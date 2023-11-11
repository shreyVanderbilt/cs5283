from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import Link

class MyTopo(Topo):
    def build(self):
        # Add two switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts to the first switch, with specific IP addresses
        h1 = self.addHost('h1', ip='192.168.1.1/24')
        h2 = self.addHost('h2', ip='192.168.1.2/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

        # Add hosts to the second switch, with specific IP addresses
        h3 = self.addHost('h3', ip='192.168.2.1/24')
        h4 = self.addHost('h4', ip='192.168.2.2/24')
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        # Connect s1 to s2 unidirectionally
        self.addLink(s1, s2)

def setupNetwork():
    "Create network and run simple performance test"
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    CLI(net)  # This line is optional, it starts a CLI for interactive debugging
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setupNetwork()
