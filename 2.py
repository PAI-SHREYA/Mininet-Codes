from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import Controller
from mininet_wifi.net import Mininet_wifi
from mininet_wifi.node import OVSKernelAP
from mininet_wifi.link import wmediumd
from mininet_wifi.wmediumdConnector import interference

def create_custom_topology():
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP, link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    # Create APs
    ap1 = net.addAccessPoint('ap1', ssid="ssid_ap1", mode="g", channel="1", position='10,20,0')
    ap2 = net.addAccessPoint('ap2', ssid="ssid_ap2", mode="g", channel="6", position='30,20,0')
    
    # Create stations
    sta1 = net.addStation('sta1', ip='10.0.0.1/8', position='5,15,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2/8', position='15,15,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3/8', position='25,15,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4/8', position='35,15,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5/8', position='20,25,0')
    sta6 = net.addStation('sta6', ip='10.0.0.6/8', position='30,25,0')

    # Add controller
    c0 = net.addController('c0')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating Links\n")
    net.addLink(ap1, ap2)
    
    # Set propagation model parameters
    net.propagationModel(model="logDistance", exp=4)

    # Plot the network graphically
    net.plotGraph(max_x=40, max_y=40)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_custom_topology()
