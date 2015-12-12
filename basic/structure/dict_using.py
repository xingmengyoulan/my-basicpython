#!/usr/bin/python

test={ '11':'111111111111',
	   '22':'222222222222',
	   '33':'333333333333',
	   '44':'444444444444',
	   '55':'555555555555'
	}
print "test is %s" % test['22']

test['00']='0000000000'

del test['33']
print '\n there are %d contacts in the adress book \n' % len(test)
for name,address in test.items():
	print 'contact %s at %s' % (name,address)
if '55' in test:
	print "\n 44: is %s " % test['44']

