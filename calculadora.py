n1 = int(input("Digite o primeiro número: ")) #primeira entrada
n2 = int(input("Digite o segundo número: "))
print()
print("""1) Adição
2) Subtração
3) Multiplicação
4) Divisão
""")
op = int(input("Qual a operação desejada? "))

if op == 1:
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")
elif op == 2:
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")
elif op == 3:
    resultado = n1 * n2
    print(f"{n1} x {n2} = {resultado}")
elif op == 4:
    resultado = n1/n2
    print(f"{n1} / {n2} = {resultado}")
