'''
Class Defination
--data members and member functions
'''
users ={} # empty dictionary
class User:
	def __init__(self,username, email, password):
		self.username=username
		self.email=email
		self.password=password
	def createUser(self):
		users[self.username]={'email': self.email, 'password': self.password}
	def listAllUsers():
		return users

user=User('Victor Omondi', 'victoromondi1997@yahoo.com', 'Vic0714343728743')
user.createUser()
print(users)