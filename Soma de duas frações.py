from math import gcd

def mmc(a, b):
    return a * b // gcd(a, b)
#def mdc(a, b):
#	return gcd(a, b)

E = [int(x) for x in input("Digite duas frações que deseja somar, entre com numerador, seguido de denominador ex{num1 den1 num2 den2}:\n").split()]
if E[1] == E[3]:
	num = E[0]+E[2]
	den = E[1]
	r2 = gcd(num, den)
	num /= r2
	den /= r2
else:
	r = mmc(E[1], E[3])
	E[0] = int((r/E[1])*E[0])
	E[2] = int((r/E[3])*E[2])
	num = E[0]+E[2]
	den = r
	r2 = gcd(num, den)
	num /= r2
	den /= r2
print(f"A soma das frações é {int(num)}/{int(den)}")