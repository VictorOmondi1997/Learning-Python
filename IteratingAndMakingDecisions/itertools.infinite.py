'''Infinite iterators allow you to 
work with a for loop in a different fashion, 
like if it was a while loop.'''

from itertools import count
for n in count(5,3):
	if n>20:
		break
	print(n, end=',')