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

    # Create routers S and T
    rS = net.addHost('rS', cls=LinuxRouter)
    rT = net.addHost('rT', cls=LinuxRouter)

    # Create routers Q R and V
    rQ = net.addHost('rQ', cls=LinuxRouter, ip='192.168.10.1/24')
    rR = net.addHost('rR', cls=LinuxRouter, ip='172.12.0.1/16')
    rV = net.addHost('rV', cls=LinuxRouter, ip='10.100.0.1/16')

    # Create routers P and U
    rP = net.addHost('rP', cls=LinuxRouter, ip='172.16.3.1/24')
    rU = net.addHost('rU', cls=LinuxRouter, ip='10.85.10.1/24')


    # Create and add LANs to the network
    lan_q_topo = SingleSwitchTopo(1)  # One host in LAN Q
    lan_r_topo = SingleSwitchTopo(1)  # One host in LAN R
    lan_v_topo = SingleSwitchTopo(1)  # One host in LAN V
    lan_q = lan_q_topo.build()
    lan_r = lan_r_topo.build()
    lan_v = lan_v_topo.build()

    # Create and add LANs to the network
    lan_p_topo = SingleSwitchTopo(2)  # Two hosts in LAN P
    lan_u_topo = SingleSwitchTopo(2)  # Two hosts in LAN U
    lan_p = lan_p_topo.build()
    lan_u = lan_u_topo.build()


    # Connect the routers to the LANs
    # Use canonical switch names
    sQ = net.addSwitch('s1')
    sR = net.addSwitch('s2')
    sV = net.addSwitch('s3')

    sP = net.addSwitch('s4')
    sU = net.addSwitch('s5')


    #Add links between routers and LANs
    net.addLink(sQ, rQ, intfName2='rP-eth1', params2={'ip': '192.168.10.1/24'})
    net.addLink(sR, rR, intfName2='rP-eth1', params2={'ip': '172.12.0.1/16'})
    net.addLink(sV, rV, intfName2='rP-eth1', params2={'ip': '10.100.0.1/16'})

    net.addLink(sP, rP, intfName2='rP-eth1', params2={'ip': '172.16.5.1/24'})
    net.addLink(sP, rP, intfName2='rP-eth2', params2={'ip': '172.16.3.1/24'})
    net.addLink(sU, rU, intfName2='rU-eth1', params2={'ip': '10.85.10.1/24'})
    net.addLink(sU, rU, intfName2='rU-eth2', params2={'ip': '10.85.8.1/24'})

    # #Add bidirectional links between the routers
    # net.addLink(rP,rQ)
    # net.addLink(rP,rR)
    # net.addLink(rQ,rV)
    # net.addLink(rQ,rS)
    # net.addLink(rR,rS)
    # net.addLink(rR,rU)
    # net.addLink(rS,rU)
    # net.addLink(rS,rV)
    # net.addLink(rT,rV)
    # net.addLink(rU,rV)
    
    # Start the network
    net.start()

    # Now configure unidirectional behavior
    # This will get the names of the interface on rQ that connects to rP
    # You should replace 'rQ-eth1' with the actual interface name that connects to rP
    rQ_interface_name = rQ.intfNames()[1]  # This assumes rQ-eth1 is the interface connected to rP

    # Block all traffic coming from rQ to rP, making the link unidirectional from rP to rQ
    # Use the actual interface name obtained from the Mininet object
    rQ.cmd(f'tc qdisc add dev {rQ_interface_name} root handle 1: netem loss 100%')

    # Configure routes on routers P and U for their second subnet
    rP.cmd('ip route add 172.16.5.0/24 dev rP-eth2')
    rU.cmd('ip route add 10.85.8.0/24 dev rU-eth2')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createTopology()
