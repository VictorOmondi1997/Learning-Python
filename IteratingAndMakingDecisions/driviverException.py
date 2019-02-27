class DriverException(Exception):
	"""docstring for ClassName"""
	pass
people = [('James', 17), ('Sylvester', 5), ("Leucrecia", 15)]
for person, age in people:
	if age>=18:
		driver=(person,age)
		break
else:
	raise DriverException('Driver Not Found')
		