from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, AP, Controller
from mn_wifi.link import wmediumd, mesh

def create_custom_topology():
    "Create a custom Mininet-WiFi network."

    # Create Mininet-WiFi network
    net = Mininet_wifi(controller=Controller, link=wmediumd, accessPoint=AP, station=Station)

    # Define switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    # Define hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')

    # Connect hosts to switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)

    # Connect switches to create redundant paths
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s1)

    return net

def test_connectivity(net):
    "Test connectivity between all hosts."

    net.pingAll()

def main():
    "Main function to create and test the network."

    # Create custom Mininet-WiFi network
    net = create_custom_topology()

    # Start the network
    net.start()

    # Test connectivity
    test_connectivity(net)

    # Start the Mininet-WiFi CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
