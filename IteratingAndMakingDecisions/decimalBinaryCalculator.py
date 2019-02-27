decimalNumber = int(input("Enter Number: "))
remainders = []
while decimalNumber > 0:
	remainder = decimalNumber % 2 #remainder of division by 2
	remainders.append(remainder) #Keep track of the remainder
	decimalNumber //= 2 #Divide Decimal Number By 2

	#Reassign the list to its reversed copy and print it
	remainders=remainders[::-1]
	print(remainders)

