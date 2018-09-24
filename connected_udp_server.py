from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):
  #If you want to send a reply back to client,uncomment startprotocol
  '''def startProtocol(self):
        host = "127.0.0.1"#localhost
        port = 1235
        comb = str(host)+","+str(port)#Python3 won't allow the double parameter so combined them in a single variable

        self.transport.connect(host,port)
        print("now we can only send to host %s port %d" % (host, port))'''

  def datagramReceived(self, data, comb):
    print(data.decode())#decode the bytes
    #self.transport.write("Server has received the message".encode())

reactor.listenUDP(1234, Helloer())
reactor.run()