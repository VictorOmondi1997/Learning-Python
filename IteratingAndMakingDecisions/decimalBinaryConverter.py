decimalNumber = int(input("Enter An Integer: "))
remainders = []
while decimalNumber>0:
	decimalNumber, remainder = divmod(decimalNumber,2)
	remainders.append(remainder)

	#remainders = remainders[::-1]
	print(remainders[-1], end="")
