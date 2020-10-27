import math


# Regra trapezio
def regraTrapezio(ListaDadosX, ListaDadosY):
    tam = len(ListaDadosX)
    div = tam - 1
    h = ((ListaDadosX[div]) - ListaDadosX[0])/div
    soma = 0
    for i in range(1, div):
        soma += ListaDadosY[i]
    resultado = (h/2)*((ListaDadosY[0]) + (ListaDadosY[div]) + (2 * (soma)))
    return resultado


# Exemplo de entrada para o programa regra trapézio
# Esse falta calcular a esse conjunto de dados de entrada "ListaDadosX" e "ListaDadosY"
ListaDadosX = [0, 0.25, 0.5, 0.75, 1]
ListaDadosY = [1.4815*10**(-1), 8.9213*10**(-2), 5.2478*10**(-2),
               2.9630*10**(-2), 1.5625*10**(-2)]

print(regraTrapezio(ListaDadosX, ListaDadosY))
