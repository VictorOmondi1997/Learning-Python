from flask import Flask
#from flask_sqlalchemy import SQLAlchemy 

#db=SQLAlchemy(app)
app= Flask(__name__)
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


@app.route("/")
def index():
	return "Victor Omondi"

if __name__ == "__main__":
    app.run(debug=True)#True to find errors during production
