#!/usr/bin/python
number=23
running=True

while running:
 guess=int(raw_input('Enter an integer:'))
 if guess==number:
	print'"congratulations,you guessed it.'
	running = False
 elif guess < number:
	print 'no,it is a litter higher than that'
 else :
	print 'no,it is a litter lower than that '
else:
	print 'the while loop is over.'
print 'Done !!!'
