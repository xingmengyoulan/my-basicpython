#!/usr/bin/python

name='abcdef'

if name.startswith('abc'):
	print 'yes,the string start with "abc"'

if 'a' in name:
	print 'yes,the contains the string "a"'

if name.find('ef') != -1 :
	print 'yew,it contains the string "war"'

delimiter='---'
mylist=['aaa','bbb','ccc','dddd']
print delimiter.join(mylist)
