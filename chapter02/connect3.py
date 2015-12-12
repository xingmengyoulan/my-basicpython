#!/usr/bin/env python
#Information Example - chapter02 - connect3.py

import socket

print "creating socket ...."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket done "

print "looking up the port number"
port = socket.getservbyname('http','tcp')
print "getservbyname done"

print "connecting to the remote host ....%d" % port
s.connect(('www.baidu.com',port))
print "connect done"

print "connected from",s.getsockname();
print "connected to",s.getpeername();
