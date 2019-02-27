name='VictorOmondi'
pairs=[(name[a],name[b])
	for a in range(len(name)) for b in range(a,len(name))
]
print(pairs)