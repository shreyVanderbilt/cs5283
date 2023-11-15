from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink

class LinuxRouter(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Enable forwarding on the router
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    "A topology with three routers and three hosts."

    def build(self, **_opts):
        # Add routers
        router1 = self.addNode('R1', cls=LinuxRouter, ip=None)
        router2 = self.addNode('R2', cls=LinuxRouter, ip=None)
        router3 = self.addNode('R3', cls=LinuxRouter, ip=None)
        
        # Add hosts
        host1 = self.addHost('H1', ip='10.0.1.1/24', defaultRoute='via 10.0.1.254')
        host2 = self.addHost('H2', ip='10.0.2.1/24', defaultRoute='via 10.0.2.254')
        host3 = self.addHost('H3', ip='10.0.4.1/24', defaultRoute='via 10.0.4.254')
        
        # Add host-router links
        self.addLink(host1, router1,
                     intfName1='H1-eth0', params1={'ip': '10.0.1.1/24'},
                     intfName2='R1-eth1', params2={'ip': '10.0.1.254/24'})
        self.addLink(host2, router2,
                     intfName1='H2-eth0', params1={'ip': '10.0.2.1/24'},
                     intfName2='R2-eth2', params2={'ip': '10.0.2.254/24'})
        self.addLink(host3, router3,
                     intfName1='H3-eth0', params1={'ip': '10.0.4.1/24'},
                     intfName2='R3-eth3', params2={'ip': '10.0.4.254/24'})
        
        # Add router-router links
        self.addLink(router1, router2,
                     intfName1='R1-eth2', params1={'ip': '10.0.3.1/24'},
                     intfName2='R2-eth1', params2={'ip': '10.0.3.2/24'})
        self.addLink(router1, router3,
                     intfName1='R1-eth3', params1={'ip': '10.0.5.1/24'},
                     intfName2='R3-eth1', params2={'ip': '10.0.5.2/24'})
        self.addLink(router2, router3,
                     intfName1='R2-eth3', params1={'ip': '10.0.6.1/24'},
                     intfName2='R3-eth2', params2={'ip': '10.0.6.2/24'})

def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet(topo=topo)
    
    info('*** Starting network\n')
    net.start()
    
    # Retrieve routers from the network
    router1 = net['R1']
    router2 = net['R2']
    router3 = net['R3']
    
    # Setup routes
    router1.cmd('ip route add 10.0.2.0/24 via 10.0.3.2')
    router2.cmd('ip route add 10.0.1.0/24 via 10.0.3.1')
    router1.cmd('ip route add 10.0.4.0/24 via 10.0.5.2')
    router3.cmd('ip route add 10.0.1.0/24 via 10.0.5.1')
    router2.cmd('ip route add 10.0.4.0/24 via 10.0.6.2')
    router3.cmd('ip route add 10.0.2.0/24 via 10.0.6.1')
    
    info('*** Running pingAll\n')
    net.pingAll()
    
    info('*** Running CLI\n')
    CLI(net)
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
