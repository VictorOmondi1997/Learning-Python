from itertools import compress
data = range(10)
even_selector=[1,0]*5
odd_selector=[0,1]*5

even_numbers=list(compress(data, even_selector))
odd_numbers=list(compress(data, odd_selector))
print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)