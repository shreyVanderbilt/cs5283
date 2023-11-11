from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel
from mininet.cli import CLI

class UniDirectionalTopo(SingleSwitchTopo):
    def build(self):
        # Create two single switch topologies
        # First single switch topology with two hosts
        SingleSwitchTopo.build(self, n=2)
        # Rename hosts and switch for the first topology
        self.hosts[0].name = 'h1'
        self.hosts[1].name = 'h2'
        self.switches[0].name = 's1'
        
        # Second single switch topology with two hosts
        SingleSwitchTopo.build(self, n=2)
        # Rename hosts and switch for the second topology
        self.hosts[2].name = 'h3'
        self.hosts[3].name = 'h4'
        self.switches[1].name = 's2'
        
        # Connect the two switches
        self.addLink('s1', 's2')

def setupNetwork():
    "Create network and run simple performance test"
    topo = UniDirectionalTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()

    # Assign specific IP addresses to the hosts
    net.get('h1').setIP('192.168.1.1', 24)
    net.get('h2').setIP('192.168.1.2', 24)
    net.get('h3').setIP('192.168.2.1', 24)
    net.get('h4').setIP('192.168.2.2', 24)

    # Setup unidirectional flow from s1 to s2
    s2 = net.get('s2')
    # Block all incoming traffic to s1 (192.168.1.0/24)
    s2.cmd('ovs-ofctl add-flow s2 priority=65535,ip,nw_dst=192.168.1.0/24,actions=drop')
    # Allow all other traffic to pass through normally
    s2.cmd('ovs-ofctl add-flow s2 priority=0,actions=normal')

    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    CLI(net)  # This line is optional, it starts a CLI for interactive debugging
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setupNetwork()
