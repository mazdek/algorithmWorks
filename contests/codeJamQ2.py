def TroubleSort( L ):
	done = False
	while not done:
		done = True
		for i in range(0, len(L) - 2):
			if L[i] > L[i+2]:
				done = False
				temp = L[i+2]
				L[i+2] = L[i]
				L[i] = temp
	return L

T = int( raw_input() )

for i in range( T ):
	retVal = -1
	nums = []
	sortedNums = []
	N = int( raw_input() )
	nums = map(int,raw_input().strip().split(' '))
	sortedNums = TroubleSort(nums)
	for j in range( len(sortedNums) - 1):
		if sortedNums[j] > sortedNums[j + 1]:
			retVal = j
			break
	if retVal == -1:
		print "Case #" + str(i + 1) + ": OK"
	else:
	 	print "Case #" + str(i + 1) + ": " + str(retVal)
