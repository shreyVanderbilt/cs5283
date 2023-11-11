from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

class CustomTopo(Topo):
    def build(self):
        # First switch with two hosts
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='192.168.1.1/24')
        h2 = self.addHost('h2', ip='192.168.1.2/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

        # Second switch with two hosts
        s2 = self.addSwitch('s2')
        h3 = self.addHost('h3', ip='192.168.2.1/24')
        h4 = self.addHost('h4', ip='192.168.2.2/24')
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        # Connect the two switches
        self.addLink(s1, s2)

def create_network():
    # Initialize Mininet with the custom topology
    net = Mininet(topo=CustomTopo(), controller=Controller, switch=OVSSwitch)

    # Start the network
    net.start()

    # Test network connectivity
    net.pingAll()

    # Run the CLI
    CLI(net)

    # After the user exits the CLI, stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
