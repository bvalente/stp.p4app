

from p4_mininet import P4Host
from p4_mininet import P4Switch
from apptopo import AppTopo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel


class STPTopo(AppTopo):

	def __init__(self):
	 super().__init__()

def main():

    net = Mininet(topo=STPTopo(), controller=None)
    net.start()
    CLI(net)



if __name__ == "__main__":
    
	setLogLevel('info')
	main()
