#!/usr/bin/env python
#Broadcast Sender - chapter 5 - broadsender.py

import socket,sys
dest = ('<broadcast>',5223)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.sendto("Hello",dest)

print "Looking for replies; press Ctrl-C  to stop."
while 1:
	(buf,address) = s.recvfrom(2048)
	if not len(buf):
		break
	print "Received from %s:%s" % (address,buf)
