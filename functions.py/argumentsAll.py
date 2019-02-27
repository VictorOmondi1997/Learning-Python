def function(a,b,c=7,*args,**kwagrs):
	print('a,b,c: \t', a,b,c)
	print('args: \t', args)
	print('kwagrs: ',kwagrs)
function(1,2,3,*(5,6,7),**{'A':'a', 'B':'b'})
function(1,2,3,5,6,7,A='a',B='b',C='c')#same as previous one