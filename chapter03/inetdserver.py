#!/usr/bin/env python
#basic inetd server - chapter - inetdserver.py

import sys
print "Welcome."
print "Please enter a strig: "
sys.stdout.flush()
line = sys.stdin.readline().strip()
print "You entered  %d characters." % len(line)

