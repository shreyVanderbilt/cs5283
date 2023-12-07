#!/usr/bin/python
#
# CS/ECE 4383/5383: Computer Networks
# Author: Aniruddha Gokhale
# Vanderbilt University
# Created: Late Fall 2023
#
# Main program for creating the custom network
#
# Run this program under "sudo" mode as
# sudo python3 custom_net.py -y <topology yaml file>
#

import os              # OS level utilities
import sys
import argparse   # for command line parsing

# Many of the packages that need to be imported. See
# https://mininet.org/api/index.html
from mininet.net import Mininet   #main network class

# other utility classes from mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.util import irange, natural, naturalSeq

# our Custom topology 
from custom_topo import CustomTopology

##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-y", "--yaml", default="topo.yaml", help="Topology YAML file, default topo.yaml")

    # parse the args
    args = parser.parse_args ()

    return args

#################################
#  main function
#################################
def main ():

  # parse command line args
  info ("Parse command line args\n")
  parsed_args = parseCmdLineArgs ()
  
  # first create my topology
  info ("Create my topology using YAML file\n")
  topo = CustomTopology (parsed_args)

  # Then create the network object from this topology. As part of this step
  # mininet will invoke the Topology's build method, which then proceeds with
  # building various parts of the topology
  info ("Create a net\n")
  net = Mininet (topo=topo)

  # fix some of the nonsensical routes
  #info ("Fix mininet-created routes at hosts that might be wrong\n")
  # Maybe it is doing things correctly and it is us who were wrong.
  #topo.fix_default_route (net)
  
  # add user-specified routes
  info ("Add user-specified routes\n")
  topo.add_routes (net)

  # Now add the iptable rules in the nat nodes
  info ("Add additional iptable rules per subnet that needs NAT access\n")
  topo.add_nat_rules (net)
  
  info ("Start the net\n")
  net.start ()  # this method must be invoked to start the mininet
  CLI (net)   # this gives us mininet prompt
  info ("Cleanup additional NAT rules\n")
  topo.cleanup_nat_rules (net)  # cleanup the additional nat rules
  info ("Stop the net\n")
  net.stop ()  # this cleans up the network

#################################
if __name__ == '__main__':
    setLogLevel ('info')
    main ()
