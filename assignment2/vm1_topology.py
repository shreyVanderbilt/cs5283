from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

class CustomTopo(Topo):
    "Custom topology with two switches and two hosts per switch."

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
    "Create the network and run the CLI."

    net = Mininet(topo=CustomTopo(), controller=Controller, switch=OVSSwitch)
    net.start()

    # Diagnostic: Dump flow tables of both switches
    print("s1 Flow Table:")
    print(net['s1'].cmd('ovs-ofctl dump-flows s1'))
    print("s2 Flow Table:")
    print(net['s2'].cmd('ovs-ofctl dump-flows s2'))

    # Test network connectivity
    print("*** Ping: testing ping reachability")
    net.pingAll()

    CLI(net)  # Start the CLI
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
