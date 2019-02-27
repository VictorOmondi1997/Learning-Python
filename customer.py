# Example customer objects
customer1 = {'id': 'abc123', 'full_name': 'John Doe'}
customer2 = {'id': 'def456', 'full_name': 'Jane Doe'}
customer3 = {'id': 'ghi789', 'full_name': 'ken Doe'}

#collect them in a tuple
cusomers = (customer1,customer2, customer3)

# or collect them in a list
cusomers = [customer1, customer2, customer3]

print(cusomers)

for custom in cusomers:
	for x in custom:
		print(x)
	print(custom)