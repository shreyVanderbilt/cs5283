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
        rP = self.addNode('rP', cls=LinuxRouter, ip='10.1.1.1/24')
        rQ = self.addNode('rQ', cls=LinuxRouter, ip='10.2.1.1/24')
        rR = self.addNode('rR', cls=LinuxRouter, ip='10.3.1.1/24')
        rS = self.addNode('rS', cls=LinuxRouter, ip='10.4.1.1/24')
        rT = self.addNode('rT', cls=LinuxRouter, ip='10.5.1.1/24')
        rU = self.addNode('rU', cls=LinuxRouter, ip='10.6.1.1/24')
        rV = self.addNode('rV', cls=LinuxRouter, ip='10.7.1.1/24')

        s1 = self.addSwitch('s1') # sP (had to rename following dpid error)
        s2 = self.addSwitch('s2') # sQ
        s3 = self.addSwitch('s3') # sR
        s4 = self.addSwitch('s4') # sS
        s5 = self.addSwitch('s5') # sT
        s6 = self.addSwitch('s6') # sU
        s7 = self.addSwitch('s7') # sV

        hP0 = self.addHost('hP0', ip='172.16.3.0/24', defaultRoute='via 10.1.1.1')
        hP2 = self.addHost('hP2', ip='172.16.5.0/24', defaultRoute='via 10.1.1.1')
        hQ0 = self.addHost('hQ0', ip='192.168.10.0/24', defaultRoute='via 10.2.1.1')
        hR2 = self.addHost('hR2', ip='172.12.0.0/16', defaultRoute='via 10.3.1.1')
        hU0 = self.addHost('hU0', ip='10.85.10.0/24', defaultRoute='via 10.6.1.1')
        hU2 = self.addHost('hU2', ip='10.85.8.0/24', defaultRoute='via 10.6.1.1')
        hV0 = self.addHost('hV0', ip='10.100.0.0/16', defaultRoute='via 10.7.1.1')

        self.addLink(hP0, s1)
        self.addLink(hP2, s2)
        self.addLink(hQ0, s3)
        self.addLink(hR2, s4)
        self.addLink(hU0, s5)
        self.addLink(hU2, s6)
        self.addLink(hV0, s7)
        
        self.addLink(s1, rP,
                intfName2='rP-sP-eth', params2={'ip':'10.1.1.1/24'})
        self.addLink(s2, rQ,
                intfName2='rQ-sQ-eth', params2={'ip':'10.1.2.1/24'})
        self.addLink(s3, rR,
                intfName2='rR-sR-eth', params2={'ip':'10.1.3.1/24'})
        self.addLink(s4, rS,
                intfName2='rS-sS-eth', params2={'ip':'10.1.4.1/24'})
        self.addLink(s5, rT,
                intfName2='rT-sT-eth', params2={'ip':'10.1.5.1/24'})
        self.addLink(s6, rU,
                intfName2='rU-sU-eth', params2={'ip':'10.1.6.1/24'})
        self.addLink(s7, rV,
                intfName2='rV-sV-eth', params2={'ip':'10.1.7.1/24'})
        
        self.addLink(rP, rQ,
                intfName1='rP-rQ-eth', params1={'ip':'10.0.10.1/24'},
                intfName2='rQ-rP-eth', params2={'ip':'10.0.10.2/24'})
        self.addLink(rP, rR,
                intfName1='rP-rR-eth', params1={'ip':'10.0.20.1/24'},
                intfName2='rR-rP-eth', params2={'ip':'10.0.20.2/24'})
        self.addLink(rQ, rS,
                intfName1='rQ-rS-eth', params1={'ip':'10.0.30.1/24'},
                intfName2='rS-rQ-eth', params2={'ip':'10.0.30.2/24'})

def run():
    # Then create the network object from this topology
    net = Mininet(topo=NetworkTopo())

    net.addNAT(name='nat1', ip='10.0.42.1').configDefault()

    net.addLink(net['rP'], net['nat1'],
                intfName1='rP-nat-eth', params1={'ip':'10.0.41.1/24'},
                intfName2='nat-rP-eth', params2={'ip':'10.0.41.2/24'})

    info(net['nat1'].cmd('ip route add 10.1.1.0/24 via 10.0.41.1 dev nat-rP-eth'))
    
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