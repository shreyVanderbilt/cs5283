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
        router1 = self.addNode('r1', cls=LinuxRouter, ip='10.1.1.1/24')
        router2 = self.addNode('r2', cls=LinuxRouter, ip='10.2.1.1/24')
        router3 = self.addNode('r3', cls=LinuxRouter, ip='10.3.1.1/24')

        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')

        host1 = self.addHost('h1', ip='10.1.1.254/24', defaultRoute='via 10.1.1.1')
        host2 = self.addHost('h2', ip='10.2.1.254/24', defaultRoute='via 10.2.1.1')
        host3 = self.addHost('h3', ip='10.3.1.254/24', defaultRoute='via 10.3.1.1')

        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(host3, switch3)

        self.addLink(switch1, router1,
                intfName2='r1-s1-eth', params2={'ip':'10.1.1.1/24'})
        self.addLink(switch2, router2,
                intfName2='r2-s2-eth', params2={'ip':'10.2.1.1/24'})
        self.addLink(switch3, router3,
                intfName2='r3-s3-eth', params2={'ip':'10.3.1.1/24'})


def run():
    # Then create the network object from this topology
    net = Mininet(topo=NetworkTopo())

    net.addNAT(name='nat1', ip='10.1.3.1').configDefault()
    net.addNAT(name='nat2', ip='10.2.3.1').configDefault()
    net.addNAT(name='nat3', ip='10.3.3.1').configDefault()

    net.addLink(net['r1'], net['nat1'],
                intfName1='r1-nat-eth', params1={'ip':'10.1.2.1/24'},
                intfName2='nat-r1-eth', params2={'ip':'10.1.2.2/24'})
    
    net.addLink(net['r2'], net['nat2'],
            intfName1='r2-nat-eth', params1={'ip':'10.2.2.1/24'},
            intfName2='nat-r2-eth', params2={'ip':'10.2.2.2/24'})
    
    net.addLink(net['r3'], net['nat3'],
            intfName1='r3-nat-eth', params1={'ip':'10.3.2.1/24'},
            intfName2='nat-r3-eth', params2={'ip':'10.3.2.2/24'})

    #NAT 1 Rule Set
    info(net['nat1'].cmd('ip route add 10.1.1.0/24 via 10.1.2.1 dev nat-r1-eth'))
    info(net['r1'].cmd('ip route add 10.1.3.0/24 via 10.1.2.2 dev r1-nat-eth'))

    info(net['r1'].cmd('ip route add default via 10.1.2.2 dev r1-nat-eth'))

    info(net['h1'].cmd('ip route add default via 10.1.1.1'))

    info(net['nat1'].cmd('ip route add default via 192.168.100.3 dev vxlan0'))

    info(net['nat1'].cmd('iptables -D FORWARD -i nat1-eth0 -d 10.1.0.0/8 -j DROP'))

    #NAT 2 Rule Set
    info(net['nat2'].cmd('ip route add 10.2.1.0/24 via 10.2.2.1 dev nat-r2-eth'))
    info(net['r2'].cmd('ip route add 10.2.3.0/24 via 10.2.2.2 dev r2-nat-eth'))

    info(net['r2'].cmd('ip route add default via 10.2.2.2 dev r2-nat-eth'))

    info(net['h2'].cmd('ip route add default via 10.2.1.1'))

    info(net['nat2'].cmd('ip route add default via 192.168.100.3 dev vxlan0'))

    info(net['nat2'].cmd('iptables -D FORWARD -i nat2-eth0 -d 10.2.0.0/8 -j DROP'))

    #NAT 3 Rule Set
    info(net['nat3'].cmd('ip route add 10.3.1.0/24 via 10.3.2.1 dev nat-r3-eth'))
    info(net['r3'].cmd('ip route add 10.3.3.0/24 via 10.3.2.2 dev r3-nat-eth'))

    info(net['r3'].cmd('ip route add default via 10.3.2.2 dev r3-nat-eth'))

    info(net['h3'].cmd('ip route add default via 10.3.1.1'))

    info(net['nat3'].cmd('ip route add default via 192.168.100.3 dev vxlan0'))

    info(net['nat3'].cmd('iptables -D FORWARD -i nat3-eth0 -d 10.3.0.0/8 -j DROP'))
    
    info( '*** Starting network\n')
    net.start ()  # this method must be invoked to start the mininet

    info('*** Running pingAll\n')
    net.pingAll()

    info( '*** Running CLI\n' )
    CLI (net)   # this gives us mininet prompt

    info( '*** Stopping network' )
    net.stop ()  # this cleans up the network


if __name__ == '__main__':
    setLogLevel('info')
    run()