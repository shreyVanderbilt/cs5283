#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.topo import Topo

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

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        for h in range(n):
            # Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h + 1),
                                cpu=.5/n)
            # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue
            self.addLink(host, switch, bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)

def createTopology():
    "Create the network."
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController('c0')

    # Create and add LANs to the network
    lan_p_topo = SingleSwitchTopo(2)  # Two hosts in LAN P
    lan_u_topo = SingleSwitchTopo(2)  # Two hosts in LAN U
    lan_p = lan_p_topo.build()
    lan_u = lan_u_topo.build()

    # Create routers
    rP = net.addHost('rP', cls=LinuxRouter, ip='172.16.3.1/24')
    rU = net.addHost('rU', cls=LinuxRouter, ip='10.85.10.1/24')

    # Connect the routers to the LANs
    # Use canonical switch names
    sP = net.addSwitch('s1')
    sU = net.addSwitch('s2')
    net.addLink(sP, rP, intfName2='rP-eth1', params2={'ip': '172.16.3.1/24'})
    net.addLink(sU, rU, intfName2='rU-eth1', params2={'ip': '10.85.10.1/24'})

    # Add a second interface to routers P and U for the second subnet
    net.addLink(sP, rP, intfName2='rP-eth2', params2={'ip': '172.16.5.1/24'})
    net.addLink(sU, rU, intfName2='rU-eth2', params2={'ip': '10.85.8.1/24'})

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
