def kwo(*a,c):
	print(a,c)
kwo(1,2,3, c=7)
kwo(c=4)
#kwo(1,2) #breaks, invalid syntax with the following error
#TypeError: kwo() missing 1 required keyword-only argument: 'c'
def kwo2(a, b=42,*,c):
	print(a,b,c)
kwo2(3,b=7,c=99)
kwo2(3,c=13)
#kwox(3,23) #breaks, invalid syntax, with the following error
#TypeErro: kwo2() missing 1 required keyword-only argument; 'c'