from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def createNetwork():
    # Create an instance of Mininet
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    # Add controller
    c0 = net.addController('c0')

    # Add hosts and switches
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start network
    net.build()
    c0.start()
    s1.start([c0])

    # Run CLI
    CLI(net)

    # Stop network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()
