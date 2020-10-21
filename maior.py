from functools import reduce

def maior(a, b):
	if a > b:
		return a
	else:
		return b

def pares(a):
	if a % 2 == 0:
		return a

array = [10, 43, 21, 100, 12]
print(reduce(maior, array))
print(list(filter(pares, array)))
