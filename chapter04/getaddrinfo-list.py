#!/usr/bin/env python
#basic getaddrinfo() not quite right list example - chapter 4
#getaddrinfo-list.py
#Takes a hostname on the command line and prints all resulting
#matches for it. Broken ; a given name may occur multiple times.

import sys,socket

# Put the list of results into the "result" variable
result = socket.getaddrinfo(sys.argv[1],None)

counter = 0
for item in result:
	#print out the address tuple for each item
	print "%-2d: %s" %(counter,item[4])
	counter += 1
