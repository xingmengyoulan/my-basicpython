#!/usr/bin/python
def func(x):
	print 'x is' ,x
	x=2
	print 'change local to',x
x=50
func(x)
print 'x is still',x


