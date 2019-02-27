def factorial(n):
	if n in (0,1):
		return 1
	result=n
	for k in range(2,n):
		result *= k
	return result
#print(factorial(16))