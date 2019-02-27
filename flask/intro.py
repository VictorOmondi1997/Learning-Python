class Person:
	def __init__(self): #Constructor
	    self.age=18
	    self.name="Victor Omondi"

	def sayHello(self):
		return "Hello" + self.name + "of age" + self.age
	def __str__(self):
		return self.name
student = Person()
print(student)	
