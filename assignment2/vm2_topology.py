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
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController('c0')

    # Create SingleSwitchTopo instances for each LAN
    lan_p_topo = SingleSwitchTopo(2)  # Two hosts in LAN P
    lan_u_topo = SingleSwitchTopo(2)  # Two hosts in LAN U

    # Create routers
    rP = net.addHost('rP', cls=LinuxRouter, ip='172.16.3.1/24')
    rU = net.addHost('rU', cls=LinuxRouter, ip='10.85.10.1/24')

    # Create and add LANs to the network
    lan_p = net.addTopo(lan_p_topo)
    lan_u = net.addTopo(lan_u_topo)

    # Connect the routers to the LANs
    for lan, router, ip in [(lan_p, rP, '172.16.3.1/24'), (lan_u, rU, '10.85.10.1/24')]:
        switch = next(iter(lan.switches()))  # Get the single switch from the LAN
        net.addLink(switch, router, intfName2='%s-eth1' % router.name, params2={'ip': ip})

    # Add a second interface to routers P and U for the second subnet
    net.addLink(net.get('sP'), rP, intfName2='rP-eth2', params2={'ip': '172.16.5.1/24'})
    net.addLink(net.get('sU'), rU, intfName2='rU-eth2', params2={'ip': '10.85.8.1/24'})

    # Start the network
    net.start()

    # Configure routes on routers P and U for their second subnet
    rP.cmd('ip route add 172.16.5.0/24 dev rP-eth2')
    rU.cmd('ip route add 10.85.8.0/24 dev rU-eth2')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createTopology()
