n =39
remainders = []
while n>0:
	remainder = n%2
	remainders.append(remainder)
	n //= 2
	remainders = remainders[::-1]
	print(remainders)