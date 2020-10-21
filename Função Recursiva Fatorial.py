def Fatorial(num):
	if num == 1 or num == 0:
		return 1
	else:
		return num * Fatorial(num-1)
Numero = int(input())
print(Fatorial(Numero))
