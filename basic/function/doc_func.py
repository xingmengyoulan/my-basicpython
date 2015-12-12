#!/usr/bin/python

def mymax(x,y):
	'''prints the max number of two numbers.
	the two valuse must be integers'''
	x = int(x)
	y = int(y)
	if x > y:
		print x,'is  max'
	else :
		print y,'is max'

print mymax(3,5)
print mymax.__doc__

