# Definição da função
import math
def f(x):
    return 2**x - x**2

# Definição da derivada da função
def g(x):
    return (2**x)* math.log(2) - 2


def newtonRaphson(x0,e,N):
    print('\n\n*** Metodo de Newton ***')
    passo = 1
    flag = 1
    condicao = True
    while condicao:
        if g(x0) == 0.0:
            print('Divisão por 0')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteração-%d, x1 = %0.6f e f(x1) = %0.6f' % (passo, x1, f(x1)))
        x0 = x1
        passo = passo + 1
        
        if passo > N:
            flag = 0
            break
        
        condicao = abs(f(x1)) > e
    
    if flag==1:
        print('\nRaiz buscada é: %0.8f' % x1)
    else:
        print('\nNão Convergiu.')



x0 = input('Chute Inicial: ')
e = input('Erro tolerável: ')
N = input('Quantidade de Passos: ')

x0 = float(x0)
e = float(e)
N = int(N)
newtonRaphson(x0,e,N)