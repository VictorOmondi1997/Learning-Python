def func_with_kwonly(a,b=42,*args,c,d=256,**kwargs):
	print('a,b: ',a,b)
	print('c,d:',c,d)
	print('args:',args)
	print('kwargs:',kwargs)
#both calls equivalent
func_with_kwonly(3,42,c=0,d=1,*(7,8,9),**{'e': 'E', 'f': 'F'})