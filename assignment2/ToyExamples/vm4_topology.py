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
        router1 = self.addNode('r1', cls=LinuxRouter, ip='10.0.4.1/24')

        switch1 = self.addSwitch('s1')

        host1 = self.addHost('h1', ip='10.0.4.254/24', defaultRoute='via 10.0.4.1')

        self.addLink(host1, switch1)

        self.addLink(switch1, router1,
                intfName2='r1-s1-eth', params2={'ip':'10.0.4.1/24'})


def run():
    # Then create the network object from this topology
    net = Mininet(topo=NetworkTopo())

    net.addNAT(name='nat1', ip='10.0.6.1').configDefault()

    net.addLink(net['r1'], net['nat1'],
                intfName1='r1-nat-eth', params1={'ip':'10.0.5.1/24'},
                intfName2='nat-r1-eth', params2={'ip':'10.0.5.2/24'})

    info(net['nat1'].cmd('ip route add 10.0.4.0/24 via 10.0.5.1 dev nat-r1-eth'))
    info(net['r1'].cmd('ip route add 10.0.6.0/24 via 10.0.5.2 dev r1-nat-eth'))

    info(net['r1'].cmd('ip route add default via 10.0.5.2 dev r1-nat-eth'))

    info(net['h1'].cmd('ip route add default via 10.0.4.1'))

    info(net['nat1'].cmd('ip route add default via 192.168.100.2 dev vxlan0'))

    info(net['nat1'].cmd('iptables -D FORWARD -i nat1-eth0 -d 10.0.0.0/8 -j DROP'))
    
    info( '*** Starting network\n')
    net.start ()  # this method must be invoked to start the mininet

    
    info( '*** Running CLI\n' )
    CLI (net)   # this gives us mininet prompt

    info( '*** Stopping network' )
    net.stop ()  # this cleans up the network


if __name__ == '__main__':
    setLogLevel('info')
    run()