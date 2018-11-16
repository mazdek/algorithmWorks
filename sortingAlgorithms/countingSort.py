def countingSort( A ):
	B = []
	A = [0] + A
	B = [0] * len(A)
	m = max(A)
	C = [0] * (m+1)
	for j in range(1,len(A)):
		C[A[j]] = C[A[j]] + 1
	for i in range(1,m+1):
		C[i] = C[i] + C[i-1]
	for j in range(len(A)-1,0,-1):
		B[C[A[j]]] = A[j]
		C[A[j]] = C[A[j]] - 1
	return B

x = []
x = list(map(int, raw_input('enter a list to sort\n').split()))
#x = [2,5,3,0,2,3,0,3]
y = countingSort( x )
print y
