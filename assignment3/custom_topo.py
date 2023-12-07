#!/usr/bin/python
#
# CS/ECE 4383/5383: Computer Networks
# Author: Aniruddha Gokhale
# Created: Fall 2023
#
#  Custom Topology creator based on YAML file 
#
# Run this program under "sudo" mode
#

# Many of the packages that need to be imported. See
# https://mininet.org/api/index.html
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node

# The following specialized ones, if needed
from mininet.node import CPULimitedHost
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.link import TCIntf

# other utility classes
from mininet.log import setLogLevel, info
from mininet.util import irange, natural, naturalSeq

# this one is for random number support
import random

# our CustomLan
from custom_lan import CustomLAN

# our utilities
import custom_utils as cu

# Linux Router
from linux_router import LinuxRouter

# Support for Yaml
import yaml

#################################################
# I don't think there is any simple way to create individual topologies in their own
# classes and then somehow combine them by picking, say, a switch from the
# child topology and connect to an artifact in the parent. So there is now only a
# single customized topology class but we have multiple methods so that the code
# is still somewhat modularized
#################################################
class CustomTopology (Topo):

  def __init__ (self, args, **_opts):
    self.topo_dict = None
    self.yaml = args.yaml  # The file containing YAML
    self.router_dict = {}   # maintains the next interface num for that router
    self.routers = []
    self.lans = []
    
    super ().__init__ (**_opts) # invoke parent class constructor

  ##############################################
  # Parses our topology description from YAML file
  ##############################################
  def parse_yaml (self):
    info ("CustomTopology::parse_yaml\n")
    with open (self.yaml, "r") as file:
      self.topo_dict = yaml.safe_load (file)['topo']
    
  ##########################################
  # build all the routers
  ##########################################
  def build_routers (self):
    '''Build the Routers one by one'''

    info ("CustomTopology::build_routers - creating all the routers\n")
    for router in self.topo_dict ['routers']:
      # add a host of Linux Router type
      info ("Router: " + router['router'] + " with IP: " + router['ip'] + "\n")
      r = self.addHost (router['router'],  # name of this router
                        cls=LinuxRouter,
                        ip=router['ip'])

      # save this router
      self.routers.append (r)

  ##########################################
  # build all the specified lans from the topo dict
  ##########################################
  def build_lans (self):
    '''Build the LANs one by one'''

    info ("CustomTopology::build_lans - creating all the LANS\n")
    for lan in self.topo_dict['lans']:
      # check if the router we are dealing with exists in our dictionary.
      # If not, create an entry and start our interface numbering from Zero
      if lan['router'] not in self.router_dict:
        self.router_dict[lan['router']] = 0

      # instantial CustomLAN object and let it build the underlying LAN
      lan_topo = CustomLAN (lan, self.router_dict[lan['router']])

      # build the lan
      lan_topo.build_lan (self)  # pass ourselves as the parent topo

      # save this LAN
      self.lans.append (lan_topo)

      # increment the interface num for this router for its next connection
      # somewhere else.
      self.router_dict[lan['router']] += 1
      
  ##########################################
  # connect the routers
  ##########################################
  def connect_routers (self):
    '''Build the LANs one by one'''

    info ("CustomTopology::connect_routers - connecting the routers\n")
    for link in self.topo_dict['links']:
      # check if the routers we are dealing with exists in our dictionary.
      # There could be a case where we have an intermediate router with
      # no LAN attached
      if link['ep1-router'] not in self.router_dict:
        self.router_dict[link['ep1-router']] = 0
      if link['ep2-router'] not in self.router_dict:
        self.router_dict[link['ep2-router']] = 0

      # retrieve the diff parts of the subnet address
      ip_prefix, prefix_len, last_octet = cu.IP_components (link['subnet'])

      # Add link
      info ("Add link between router " + link['ep1-router'] + " and router " + link['ep2-router'] + "\n")
      self.addLink (link['ep1-router'],
                    link['ep2-router'],
                    intfName1=link['ep1-router'] + "-eth" + str (self.router_dict[link['ep1-router']]),
                    params1={"ip": ip_prefix + "1" + prefix_len},
                    intfName2=link['ep2-router'] + "-eth" + str (self.router_dict[link['ep2-router']]),
                    params2={"ip": ip_prefix + "2" + prefix_len})
      
      # increment the interface num for these routers
      self.router_dict[link['ep1-router']] += 1
      self.router_dict[link['ep2-router']] += 1
      
  ##########################################
  # Fix routing rules at the individual hosts
  #
  # For reasons that I have not yet figured out, Mininet seems to force
  # upon each LAN host a default route to the default IP Base of 10.0.0.0/8
  # despite providing a defaultRoute going thru the specified router.
  #
  # This has happened sometimes.
  #
  # Thus, we use this brute force approach to fix the routes.
  ##########################################
  def fix_default_route (self, net):
    '''Fix default routing entries for each LAN '''

    info ("CustomTopology::fix_default_routes on each LAN host in our topology\n")
    info ("Currenly a NO-OP\n")

  ##########################################
  # Add user-supplied routing table entries
  ##########################################
  def add_routes (self, net):
    '''Add routing entries'''

    info ("CustomTopology::add_routes - update routing entries\n")

    for route in self.topo_dict['routes']:
      info ("Routing table update for Router: " + route['router'] + "\n")
      for entry in route['entries']:
        info ("Adding entry: " + entry + "\n")
        net[route['router']].cmd ("ip route add " + entry)

    # Although the LinuxRouter class's config method sets the IPv4 forwarding=1
    # I think that this is not getting enabled. So we do it again here for each of
    # the routers in our topology
    info ("CustomTopology::add_routes - enable forwarding in our routers\n")
    for router in self.routers:
      info ("Enabling IPv4 forwarding for router: " + router + "\n")
      net[router].cmd ("sysctl net.ipv4.ip_forward=1")
    
  ##########################################
  # Add NAT rules to all the subnets that need NAT access
  ##########################################
  def add_nat_rules (self, net):
    '''Add NAT rules'''

    info ("CustomTopology::add_nat_rules - add NAT rules for specified subnets\n")

    for nat in self.topo_dict['nats']:
      info ("Adding NAT rules for nat node: " + nat['name'] + "\n")
      nat_node = nat['name']
      nat_intf = nat_node + "-eth0"
      for subnet in nat['subnets']:
        info ("Adding rules for subnet: " + subnet + "\n")
        net[nat_node].cmd( 'iptables -I FORWARD',
                           '-i', nat_intf, '-d', subnet, '-j DROP' )
        net[nat_node].cmd( 'iptables -A FORWARD',
                           '-i', nat_intf, '-s', subnet, '-j ACCEPT' )
        net[nat_node].cmd( 'iptables -A FORWARD',
                           '-o', nat_intf, '-d', subnet, '-j ACCEPT' )
        net[nat_node].cmd( 'iptables -t nat -A POSTROUTING',
                           '-s', subnet, "'!'", '-d', subnet, '-j MASQUERADE' )

  ##########################################
  # Cleanup additional NAT rules that we had added. The default one
  # will (should) get cleaned up as part of mininet NAT node's terminate
  # method
  ##########################################
  def cleanup_nat_rules (self, net):
    '''Cleanup the additional NAT rules'''

    info ("CustomTopology::cleanup_nat_rules - cleanup NAT rules for specified subnets\n")

    for nat in self.topo_dict['nats']:
      info ("Cleaning up NAT rules for nat node: " + nat['name'] + "\n")
      nat_node = nat['name']
      nat_intf = nat_node + "-eth0"
      for subnet in nat['subnets']:
        info ("Cleaning up rules for subnet: " + subnet + "\n")
        net[nat_node].cmd( 'iptables -D FORWARD',
                           '-i', nat_intf, '-d', subnet, '-j DROP' )
        net[nat_node].cmd( 'iptables -D FORWARD',
                           '-i', nat_intf, '-s', subnet, '-j ACCEPT' )
        net[nat_node].cmd( 'iptables -D FORWARD',
                           '-o', nat_intf, '-d', subnet, '-j ACCEPT' )
        net[nat_node].cmd( 'iptables -t nat -D POSTROUTING',
                           '-s', subnet, "'!'", '-d', subnet, '-j MASQUERADE' )

  ##########################################
  # The overridden build method
  ##########################################
  def build (self, **_opts):
    # Let us create single switch topology and specify a subnet they will use

    info ("CustomTopology::build - start building\n")

    # parse the yaml
    self.parse_yaml ()

    # first, build the routers
    self.build_routers ()

    # next, build the LANs
    self.build_lans ()
    
    # next, make connections between routers
    self.connect_routers ()

    # other operations will be performed after the net is formed
