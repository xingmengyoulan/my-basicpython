#!/usr/bin/env python
#basic getaddrinfo() basic example - chapter 4 - getaddrinfo-basic.py
import sys,socket

result = socket.getaddrinfo(sys.argv[1],None)
print result[0][4]
print result[0][0]
print result[0][1]
print result[0][2]
print result[0][3]
