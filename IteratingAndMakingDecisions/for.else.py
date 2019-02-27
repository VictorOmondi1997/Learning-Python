class DriverException(Exception):
	pass
people = [('James', 17), ('Sylverster', 9), ('Leucrecia', 10), ('Shirley', 10)]
for person, age in people:
	if age>=18:
		driver=(person, age)
		break
else: 
	raise DriverException('Driver not found')