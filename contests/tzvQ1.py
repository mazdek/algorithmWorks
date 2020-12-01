from itertools import combinations

def toggle(x):
	if x:
		return 0
	else:
		return 1

def toggleTri(l,x):
	l[x-1] = toggle(l[x-1])
	l[x] = toggle(l[x])
	l[x+1] = toggle(l[x+1])
	return l

a = []
coms = []
for i in xrange(1,10):
	a = list(combinations(range(1,10),i))
	for j in range(len(a)):
		coms.append(a[j])

def isOne(l):
	for i in xrange(1,10):
		if l[i] == 0:
			return False
	return True

for i in range(len(coms)):
	lamps = [0,0,1,0,0,0,1,0,0,0,0]
	for j in range(len(coms[i])):
		toggleTri(lamps,coms[i][j])
	if isOne(lamps):
		print coms[i]
