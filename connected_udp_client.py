from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"#localhost
        port = 1234
        comb = str(host)+","+str(port)#Python3 won't allow the double parameter so combined them in a single variable

        self.transport.connect(host,port)
        print("now we can only send to host %s port %d" % (host, port))
        self.transport.write("Hello World".encode())

    def datagramReceived(self, data, comb):
        print (data.decode())

    def connectionRefused(self):
        print ("No one listening")

reactor.listenUDP(1235, Helloer())
reactor.run()