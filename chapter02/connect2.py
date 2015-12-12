#!/usr/bin/env python
#Revised Connection Example - Chapter 2 - connect2.py

import socket

print "creating socket ..."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
print " socket done"

print "looking up port number..."
port = socket.getservbyname('http','tcp');
print "getservbyname done"

print "connecting to remote host on port %d..." % port,
s.connect(("www.baidu.com",port))
print "connect done"

