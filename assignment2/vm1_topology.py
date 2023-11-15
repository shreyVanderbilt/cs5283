from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link

def create_network():
    "Create a network with two switches and four hosts."

    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    print("*** Creating nodes")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.1.1/24')
    h4 = net.addHost('h4', ip='10.0.1.2/24')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    print("*** Creating links")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)  # Link between switches

    print("*** Starting network")
    net.build()
    net.addController('c0')

    print("*** Testing network connectivity")
    net.pingAll()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
