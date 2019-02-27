#using map and filter
print(list(filter(lambda n: not n%2, map(lambda n: n**2, range(20)))))
#equivalent, but using list compression
#sq2=[n**2 for n in range(10) if not n%2]