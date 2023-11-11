#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_network():
    # Create an instance of the network
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)
    
    # Add a controller
    c0 = net.addController('c0')
    
    # Add two hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    
    # Add two switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    
    # Create links between hosts and switches
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    
    # Create a link between switches to allow communication between hosts
    net.addLink(s1, s2)
    
    # Start the network
    net.start()
    
    # Test network connectivity
    net.pingAll()
    
    # Drop the user in a CLI so they can try other commands
    CLI(net)
    
    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # Set the log level to info to see more detailed output
    create_network()
