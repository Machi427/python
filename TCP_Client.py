# -*- coding: utf-8 -*-

import socket

target_host = "www.google.com"
target_port = 80

#create s "socket_object"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client.connect((target_host,target_port))

#send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#response data
response = client.recv(4096)

print response