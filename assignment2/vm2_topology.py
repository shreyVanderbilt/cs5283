#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.topo import SingleSwitchTopo

class LinuxRouter(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        # Disable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

def createTopology():
    "Create the network."
    
    # Create SingleSwitchTopo instances for each LAN
    lan_p_topo = SingleSwitchTopo(2)  # Two hosts in LAN P
    lan_u_topo = SingleSwitchTopo(2)  # Two hosts in LAN U

    # Create a Mininet instance for each LAN
    net_p = Mininet(topo=lan_p_topo, controller=Controller, switch=OVSSwitch, link=TCLink)
    net_u = Mininet(topo=lan_u_topo, controller=Controller, switch=OVSSwitch, link=TCLink)

    # Start the network for LAN P and U
    net_p.start()
    net_u.start()

    # Note: You will need to merge the two Mininet instances or design your network to be within a single Mininet instance.
    # This example shows how to start two separate Mininet instances, which is not typical usage.
    # You will need to interconnect these LANs through routers or switches manually.

    # Add controller
    c0 = net_p.addController('c0')

    # Create routers with multiple IP addresses
    rP = net_p.addHost('rP', cls=LinuxRouter, ip='172.16.3.1/24')
    rU = net_u.addHost('rU', cls=LinuxRouter, ip='10.85.10.1/24')

    # Configure IP addresses for routers
    rP.cmd('ifconfig rP-eth0 172.16.3.1/24')
    rP.cmd('ifconfig rP-eth0:0 172.16.5.1/24')  # Virtual interface for the second IP
    rU.cmd('ifconfig rU-eth0 10.85.10.1/24')
    rU.cmd('ifconfig rU-eth0:0 10.85.8.1/24')   # Virtual interface for the second IP

    # Assuming you have switches or routers to interconnect LAN P and LAN U
    # You will need to create those and connect them appropriately here.

    CLI(net_p)
    CLI(net_u)
    net_p.stop()
    net_u.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createTopology()
