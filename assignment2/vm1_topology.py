from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.cli import CLI

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

    # Setup unidirectional flow from s1 to s2 by adding OpenFlow rules to drop packets from s2 to s1
    s2 = net.get('s2')
    s2.cmd('ovs-ofctl add-flow s2 priority=65535,ip,nw_src=192.168.2.0/24,nw_dst=192.168.1.0/24,actions=drop')
    s2.cmd('ovs-ofctl add-flow s2 priority=0,actions=normal')

    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    CLI(net)  # Optionally start a CLI for interactive debugging
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setupNetwork()
