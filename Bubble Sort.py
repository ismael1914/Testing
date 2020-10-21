quantidade = int(input('Digite o número de elementos do vetor\n'))
A = input("Entre com o vetor que será ordenado:\n").split(' ')
passagens = len(A)-1
for i in range(len(A)-1):
	for j in range(passagens, 0, -1):
		if int(A[j]) < int(A[j-1]):
			A[j-1], A[j] = A[j], A[j-1]
for i in A:
	print(i, end=' ')
