def calculatePriceWithVAT(price, vat):
	return price*(100+vat)/100

print(calculatePriceWithVAT(500,20))