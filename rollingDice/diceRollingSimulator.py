from random import randint

def run():
	while True:
		number = integerInput("Enter A Number To Roll: ")
		if validate(number):
			return "Game Terminated"
		roll = randint(1,6)
		print(formatResult(roll))
def integerInput(message):
	while True:
		try:
			x=int(input(message))
			return x
		except ValueError:
			print("\nError, Please An integer Between 1-6 ")
def validate(number):
	return number==0
def formatResult(number):
	return f"Result {number}"
