#!/usr/bin/env python
#NOnblocking I/O witch select() - chapter 5 - selectclient.py

import  socket, sys, select

port = 5222
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1

def spin():
	global spinsize, spinpos, spindir
	spinstr = '.' * spinpos + \
			  '|' + '.' * (spinsize - spinpos -1)
	print "spinstr:" + spinstr
	
	sys.stdout.write('\r' +spinstr + ' ')
	spindsys.stdout.flush()
	
	spinpos += spindir
	if spinpos < 0:
		spindir = 1
		spinpos = 1
	elif spinpos >= spinsize:
		spinpos -= 2
		spindir = -1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
	infds,outfds,errfds = select.select([s],[],[s],0.05)
	if len(infds):
		data = s.recv(4096)
		if not len(data):
				print("\rRemote end close connection;exiting.")
				break
		sys.stdout,write("\r Received: " + data)
		sys.stdout.flush()
	if len(errfds):
		print "\rProblem occurred;exiting."
		sys.exit(0)
	spin()
