#!/usr/bin/env python
#Basic Connection Example -	Chapter02 - connect.py

import socket

print "creating socket ....."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket done."

print "connecting to remote host..."
s.connect(("www.baidu.com",80))
print "conect done"

sleep(200)
