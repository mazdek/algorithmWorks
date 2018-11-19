n = int( raw_input() ) 

def currentDamage( ins ):
	retVal = 0
	curShot = 1
	powOfTwo = [0]
	for i in ins:
		if i == 'S':
			retVal += curShot
			if len(powOfTwo) > 0:
				powOfTwo[-1] += 1
		elif i == 'C':
			curShot *= 2
			powOfTwo.append( 0 )
	return retVal, powOfTwo

for i in range(n):
	powTwo = []
	line = raw_input()
	D, instructions = line.split(' ')
	D = int(D)
	T, powTwo = currentDamage(instructions)
	if sum(powTwo) > D:
		print "Case #" + str(i+1) +": "+ "IMPOSSIBLE"
	elif D >= T:
		print  "Case #" + str(i+1) +": "+ "0"
	else:
		numOfSubs = 0
		for j in range(len(powTwo) -1, 0, -1):
			if (T - pow(2,j-1)*powTwo[j]) > D:
				powTwo[j-1] += powTwo[j]
				numOfSubs += powTwo[j]
				T -= pow(2,j-1)*powTwo[j]
				powTwo[j] = 0
			else:
				for x in range(powTwo[j]):
					powTwo[j-1] += 1
					numOfSubs += 1
					T -= pow(2,j-1)
					powTwo[j] -=1
					if T <= D:
						break
				break
		print "Case #" + str(i+1) +": "+ str(numOfSubs)
