# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
target_port = 80

#create s "socket_object"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect to server
client.connect((target_host,target_port))

#send data
client.sendto("AAABBBCCC", (target_host,target_port))

#response data
response = client.recv(4096)

print response