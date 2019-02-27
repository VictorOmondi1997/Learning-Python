fName='Victor'
pairs=[]

for a in range(len(fName)):
	for b in range(a,len(fName)):
		pairs.append((fName[a], fName[b]))
print(pairs)