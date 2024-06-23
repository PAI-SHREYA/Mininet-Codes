from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.cli import CLI
from mininet.link import TCLink

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # Add links between switches to create redundancy
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)

        # Add links between switches and hosts
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=OVSController, link=TCLink)
    net.start()
    
    # Test connectivity
    print("Testing network connectivity")
    net.pingAll()

    # Start CLI
    CLI(net)

    net.stop()

if __name__ == '__main__':
    run()
