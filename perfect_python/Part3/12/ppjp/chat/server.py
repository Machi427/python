
import asyncore

class EchoHandler(asyncore.dispatcher_with_send):

    def __init__(self, socket, parent):
        super(EchoHandler, self).__init__(socket)
        self.parent = parent

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.parent.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.handlers = []
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)
        self.handlers.append(handler)

    def send(self, data):
        for handler in self.handlers:
            handler.send(data)

server = EchoServer('localhost', 8080)
asyncore.loop()

