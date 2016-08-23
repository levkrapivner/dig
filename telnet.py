#!/usr/bin/python
import socket

Ip = raw_input("Insert Ip please --->  ")
server = socket.gethostbyaddr(Ip)
print server[0]
