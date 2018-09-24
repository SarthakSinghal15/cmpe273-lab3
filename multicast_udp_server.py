from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingPong(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagrams, address):
        print(datagrams.decode())
        #uncomment below line if server has to send response in the channel
        '''if datagrams.decode() == "Hello World":
            self.transport.write("Message received by the server".encode(), ("228.0.0.5", 8005))'''

reactor.listenMulticast(8005, MulticastPingPong(),listenMultiple=True)
reactor.run()