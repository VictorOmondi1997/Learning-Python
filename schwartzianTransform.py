students = [
	dict(id=0, credits=dict(math=9, physics=6, history=7)),
	dict(id=1, credits=dict(math=6, physics=7, latin=10)),
	dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
	dict(id=3, credits=dict(math=5, physics=5, history=7)),
]

def decorate(student):
	#create a 2-tuple (sum of credits, student) from dict
	return (sum(student['credits'].values()),student)

def undecorate(decoratedStudent):
	#discard sum or credits, retun original student dict
	return decoratedStudent[1]
students=sorted(map(decorate, students), reverse=True)
students=list(map(undecorate, students))


