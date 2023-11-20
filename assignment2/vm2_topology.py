#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter (Node):
    def config (self, **params):
        super (LinuxRouter, self).config (**params)
        self.cmd ('sysctl net.ipv4.ip_forward=1')

    def terminate (self):
        self.cmd ('sysctl net.ipv4.ip_forward=0')
        super (LinuxRouter, self).terminate ()


class NetworkTopo (Topo):

    def build(self, **_opts):

        router1 = self.addNode('r1', cls=LinuxRouter, ip='10.0.10.1/24')
        switch1 = self.addSwitch('s1')
        host1 = self.addHost('h1', ip='10.0.10.254/24', defaultRoute='via 10.0.10.1')
        self.addLink(host1, switch1)
        self.addLink(switch1, router1,
                intfName2='r1-s1-eth', params2={'ip':'10.0.10.1/24'})
        
        router2 = self.addNode('r2', cls=LinuxRouter, ip='10.0.20.1/24')
        switch2 = self.addSwitch('s2')
        host2 = self.addHost('h2', ip='10.0.20.254/24', defaultRoute='via 10.0.20.1')
        self.addLink(host2, switch2)
        self.addLink(switch2, router2,
                intfName2='r2-s2-eth', params2={'ip':'10.0.20.1/24'})

        router3 = self.addNode('r3', cls=LinuxRouter, ip='10.0.30.1/24')
        switch3 = self.addSwitch('s3')
        host3 = self.addHost('h3', ip='10.0.30.254/24', defaultRoute='via 10.0.30.1')
        self.addLink(host3, switch3)
        self.addLink(switch3, router3,
                intfName2='r3-s3-eth', params2={'ip':'10.0.30.1/24'})

        router4 = self.addNode('r4', cls=LinuxRouter, ip='10.0.40.1/24')
        switch4 = self.addSwitch('s4')
        host4 = self.addHost('h4', ip='10.0.40.254/24', defaultRoute='via 10.0.40.1')
        self.addLink(host4, switch4)
        self.addLink(switch4, router4,
                intfName2='r4-s4-eth', params2={'ip':'10.0.40.1/24'})

        router5 = self.addNode('r5', cls=LinuxRouter, ip='10.0.50.1/24')
        switch5 = self.addSwitch('s5')
        host5 = self.addHost('h5', ip='10.0.50.254/24', defaultRoute='via 10.0.50.1')
        self.addLink(host5, switch5)
        self.addLink(switch5, router5,
                intfName2='r5-s5-eth', params2={'ip':'10.0.50.1/24'})

        router6 = self.addNode('r6', cls=LinuxRouter, ip='10.0.60.1/24')
        switch6 = self.addSwitch('s6')        
        host6 = self.addHost('h6', ip='10.0.60.254/24', defaultRoute='via 10.0.60.1')
        self.addLink(host6, switch6)
        self.addLink(switch6, router6,
                intfName2='r6-s6-eth', params2={'ip':'10.0.60.1/24'})

        router7 = self.addNode('r7', cls=LinuxRouter, ip='10.0.70.1/24')
        switch7 = self.addSwitch('s7')
        host7 = self.addHost('h7', ip='10.0.70.254/24', defaultRoute='via 10.0.70.1')
        self.addLink(host7, switch7)
        self.addLink(switch7, router7,
                intfName2='r7-s7-eth', params2={'ip':'10.0.70.1/24'})

        router8 = self.addNode('r8', cls=LinuxRouter, ip='10.0.80.1/24')
        switch8 = self.addSwitch('s8')
        host8 = self.addHost('h8', ip='10.0.80.254/24', defaultRoute='via 10.0.80.1')
        self.addLink(host8, switch8)
        self.addLink(switch8, router8,
                intfName2='r8-s8-eth', params2={'ip':'10.0.80.1/24'})
        
        self.addLink(router3, router1,
                intfName1='r3-r1-eth', params1={'ip':'10.0.44.1/24'},
                intfName2='r1-r3-eth', params2={'ip':'10.0.44.2/24'})

def run():
    # Then create the network object from this topology
    net = Mininet(topo=NetworkTopo())

    net.addNAT(name='nat1', ip='10.0.42.1').configDefault()

    net.addLink(net['r1'], net['nat1'],
                intfName1='r1-nat-eth', params1={'ip':'10.0.41.1/24'},
                intfName2='nat-r1-eth', params2={'ip':'10.0.41.2/24'})

    info(net['nat1'].cmd('ip route add 10.0.10.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.20.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.30.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.40.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.50.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.60.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.70.0/24 via 10.0.41.1 dev nat-r1-eth'))
    info(net['nat1'].cmd('ip route add 10.0.80.0/24 via 10.0.41.1 dev nat-r1-eth'))

    info(net['r1'].cmd('ip route add 10.0.42.0/24 via 10.0.41.2 dev r1-nat-eth')) 
    info(net['r3'].cmd('ip route add 10.0.42.0/24 via 10.0.44.2 dev r3-r1-eth'))  

    info(net['r1'].cmd('ip route add default via 10.0.41.2 dev r1-nat-eth'))
    info(net['r1'].cmd('ip route add 10.0.20.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.30.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.40.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.50.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.60.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.70.0/24 via 10.0.44.1 dev r1-r3-eth'))
    info(net['r1'].cmd('ip route add 10.0.80.0/24 via 10.0.44.1 dev r1-r3-eth'))

    info(net['h1'].cmd('ip route add default via 10.0.10.1'))

    info(net['nat1'].cmd('ip route add default via 192.168.100.2 dev vxlan0'))

    info(net['nat1'].cmd('iptables -D FORWARD -i nat1-eth0 -d 10.0.0.0/8 -j DROP'))
    
    info( '*** Starting network\n')
    net.start()

    info('*** Running pingAll\n')
    net.pingAll()

    info( '*** Running CLI\n' )
    CLI(net)

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()