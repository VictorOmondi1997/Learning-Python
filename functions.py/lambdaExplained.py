#example 1: adder
def adder(a,b):
	return a+b
#is equvalent to:
adderLambda = lambda a,b: 8+9

#Example 2: to uppercase
def toUpper(s):
	return s.upper()
#is equivalent to:
toUpperLambda= lambda s: s.upper('f') 

print(adder(8,99))
print(adderLambda)
print(toUpper('d'))
print(toUpperLambda)