'''A prime number (or Prime is a 
Natural number greater than 1 that has no 
positive divisors other than 1 and it self.
A natural number greater than 1 that is not a prime number is
called a composite number'''
primes =[]#this wil contain the primes in the end
upto=3000 #the limit, inclusive
for n in range(2,upto+1):
	is_prime=True #flag, new at eact iteration of outer for
	for divisor in range(2,n):
		if n%divisor==0:
			is_prime=False
			break
	if is_prime: #check on flag
	    primes.append(n)
print(primes)