def getMultiplesOfFive(n):
	return list(filter(lambda k: not k%5, range(n)))
print(getMultiplesOfFive(590))