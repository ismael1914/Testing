def binarySearch(alist, elem):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		if alist[midpoint] == elem:
			return True
		else:
			if elem < alist[midpoint]:
				return binarySearch(alist[:midpoint], elem)
			else:
				return binarySearch(alist[midpoint+1:], elem)

alist = [1, 10, 14, 21, 34, 55, 61, 66, 81, 99, 111, 132]
entrada = int(input("Digite um número e verifique se está no vetor: "))
if binarySearch(alist, entrada):
	print(f"O elemento {entrada} está na lista")
else:
	print(f"O elemento {entrada} não está na lista")