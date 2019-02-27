from math import sqrt, ceil
def getPrimes(n):
	'''Calculate a list of primes up to n(included'''
	primelist=[]
	for candidate in range(2,n+1):
		isPrime=True
		root=int(ceil(sqrt(candidate)))#division limit
		for prime in primelist: #we try only the priems
			if prime>root:
				break
			if candidate%prime ==0:
				isPrime=False
				break
		if isPrime:
			primelist.append(candidate)
	return primelist

print(getPrimes(1200))