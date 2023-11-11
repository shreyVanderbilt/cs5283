from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.util import dumpNodeConnections

class UniDirectionalTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts to the first switch with specific IPs
        h1 = self.addHost('h1', ip='192.168.1.1/24')
        h2 = self.addHost('h2', ip='192.168.1.2/24')
        # Add hosts to the second switch with specific IPs
        h3 = self.addHost('h3', ip='192.168.2.1/24')
        h4 = self.addHost('h4', ip='192.168.2.2/24')

        # Add links between hosts and their respective switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        # Connect the two switches
        self.addLink(s1, s2)

def setupNetwork():
    "Create a network with unidirectional flow from s1 to s2"
    topo = UniDirectionalTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()

    # Adding static routes to hosts on s1 for subnet on s2
    net['h1'].cmd('route add -net 192.168.2.0 netmask 255.255.255.0 dev h1-eth0')
    net['h2'].cmd('route add -net 192.168.2.0 netmask 255.255.255.0 dev h2-eth0')

    # Adding static routes to hosts on s2 for subnet on s1
    # This is only needed if you want bidirectional communication
    # net['h3'].cmd('route add -net 192.168.1.0 netmask 255.255.255.0 dev h3-eth0')
    # net['h4'].cmd('route add -net 192.168.1.0 netmask 255.255.255.0 dev h4-eth0')

    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    CLI(net)  # Optionally start a CLI for interactive debugging
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setupNetwork()
