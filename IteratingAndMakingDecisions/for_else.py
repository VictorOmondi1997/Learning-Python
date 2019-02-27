class DriverException(Exception):
	"""docstring for ClassName"""
	pass

people = [('James',21), ('Sylverster',20), ('Leucrecia', 10), ('Robert',80)]
driver = None
for person, age in people:
	if age>=18:
		driver=(person, age)
	if driver is None:
		raise DriverException('Driver Not Found')
