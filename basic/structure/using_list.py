#!/usr/bin/python
shoplist=['apple','mango','carrot','banana']

print 'I have',len(shoplist),'items to purchase.'

print 'These item sare:'
for item in shoplist:
	print item
print '\n I also have to buy rice.'
shoplist.append('rice')
print 'my shopping list is now',shoplist

print 'I will sort my list now '
shoplist.sort()
print 'sorted shopping list i',shoplist

print 'the first item I will buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the ',olditem
print 'My shopping list is now',shoplist

