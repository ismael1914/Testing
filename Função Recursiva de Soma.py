def Soma(Num):
	if Num == 1:
		return 1
	else:
		return Num + Soma(Num-1)
N = int(input())
print(Soma(N))