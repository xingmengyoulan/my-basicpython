#!/usr/bin/python

zoo=('wolf','elephant','penguin')
print 'number of animals in the zoo is',len(zoo)

new_zoo=('monkey','dolphin',zoo)
print 'number of animals int the new zoo is',len(new_zoo)
print 'animals in new zoo are ',new_zoo
print 'animals brought from old zoo are',new_zoo[2]
print 'animals brought from old zoo is ',new_zoo[2][2]
print 'animals brought from old zoo is ',new_zoo[2][1]
print 'animals brought from old zoo is ',new_zoo[2][0]
print 'animals brought from old zoo is ',new_zoo[1][1]

