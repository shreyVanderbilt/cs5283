from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, OVSKernelSwitch
from mininet.link import TCLink

class CustomTopology(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        self.addLink(s1, s2, cls=TCLink)
        self.addLink(s1, h1)
        self.addLink(s2, h2)

def main():
    topo = CustomTopology()
    net = Mininet(topo=topo, controller=Controller, switch=OVSKernelSwitch)

    net.start()

    # Add a flow rule to block traffic from s2 to s1
    s1 = net.get('s1')
    s1.cmd('ovs-ofctl -O OpenFlow13 add-flow s1 "in_port=2,actions=drop"')

    # Test the network
    net.pingAll()

    # Cleanup
    s1.cmd('ovs-ofctl -O OpenFlow13 del-flows s1 "in_port=2"')  # Remove the block
    net.stop()

if __name__ == '__main__':
    main()
