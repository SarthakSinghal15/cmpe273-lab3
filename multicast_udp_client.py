from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        self.transport.joinGroup("228.0.0.5")
        self.transport.write("Hello World".encode(), ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print ("Datagram %s received from %s" % (repr(datagram), repr(address)))


reactor.listenMulticast(8005, MulticastPingClient(), listenMultiple=True)
reactor.run()