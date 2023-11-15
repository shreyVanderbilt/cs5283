from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink

def run():
    "Create network and run simple performance test"
    net = Mininet( link=TCLink )
    
    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='192.168.1.2/24', defaultRoute='via 192.168.1.1' )
    h2 = net.addHost( 'h2', ip='192.168.2.2/24', defaultRoute='via 192.168.2.1' )

    info( '*** Adding routers\n' )
    r1 = net.addHost( 'r1', ip='192.168.1.1/24' )
    r2 = net.addHost( 'r2', ip='192.168.2.1/24' )

    info( '*** Creating links\n' )
    net.addLink( h1, r1 )
    net.addLink( h2, r2 )
    net.addLink( r1, r2 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Configuring routers\n' )
    r1.cmd( 'ifconfig r1-eth1 10.0.0.1/24' )
    r2.cmd( 'ifconfig r2-eth1 10.0.0.2/24' )

    info( '*** Enabling forwarding on routers\n' )
    r1.cmd( 'echo 1 > /proc/sys/net/ipv4/ip_forward' )
    r2.cmd( 'echo 1 > /proc/sys/net/ipv4/ip_forward' )

    info( '*** Adding routes\n' )
    h1.cmd( 'route add default gw 192.168.1.1' )
    h2.cmd( 'route add default gw 192.168.2.1' )
    r1.cmd( 'route add -net 192.168.2.0/24 gw 10.0.0.2' )
    r2.cmd( 'route add -net 192.168.1.0/24 gw 10.0.0.1' )

    info( '*** Running pingAll\n' )
    net.pingAll()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network\n' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
