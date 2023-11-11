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
    
    # Add three hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='100.100.0.1')
    
    # Add two switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    
    # Create links between hosts and switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2) 
    
    # Create a link between switches to allow communication between hosts
    net.addLink(s1, s2)
    
    # Start the network
    net.start()
    
    # Run the command to block traffic on switch s2
    s2 = net.get('s2')
    s2.cmd('ovs-ofctl add-flow s2 priority=100,table=0,ip,nw_src=10.0.0.0/24,actions=normal')

    # Test network connectivity
    net.pingAll()
    
    # Drop the user in a CLI so they can try other commands
    CLI(net)
    
    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # Set the log level to info to see more detailed output
    create_network()
