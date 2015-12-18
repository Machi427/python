# -*- coding:utf-8 -*-
import asyncore
import sys

class EchoClient(asyncore.dispatcher_with_send):
   def __init__(self, message):
       asyncore.dispatcher_with_send.__init__(self)
       self.message = message
       self.create_socket()
   
   def handle_write(self):
       self.send(self.message.encode('utf-8'))

   def handle_read(self):
       data = self.recv(8192)
       print(data.decode('utf-8'))
       self.close()

   def handle_close(self):
       sys.exit(0)

client = EchoClient("こんにちわ")
client.connect(('localhost', 8080))
asyncore.loop()
