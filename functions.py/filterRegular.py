def isMultipleOfFive(n):
	return not n%5
def getMultiplesOfFive(n):
	return list(filter(isMultipleOfFive, range(n)))
print(getMultiplesOfFive(590))