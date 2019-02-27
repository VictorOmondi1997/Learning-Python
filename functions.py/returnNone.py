def function():
	pass
function()#the return of this call wont be collected. it's lost
a=function() # the return of this on instead is collected into `a`
print(a)#prints: None
