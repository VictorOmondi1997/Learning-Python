def func(**kwargs):
	print(kwargs)
#all cals equivalent. They print: {'a': 1, 'b': 42}
func(a=1,b=42)
func(**{'a':1,'b':42})
func(**dict(a=1,b=42))