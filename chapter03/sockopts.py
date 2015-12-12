#!/usr/bin/env python
#Get list of available socket options --chapter03 --sockopts.py

import socket
socklist = [x for x in dir(socket) if x.startswitch('SO_')]
socklist.sort()
for x in socklist:
	print x

