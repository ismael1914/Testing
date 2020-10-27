import random
import math

Pontos_no_Quadrado = 1000000 #Distribuição dos números aleatórios
Pontos_no_Circulo = 0

init = 1
while init <=Pontos_no_Quadrado:
    #Geração de Coordenadas, respeitando o raio = 2
    PontoX=random.uniform(0,2)
    PontoY=random.uniform(0,2)
    deltaX= math.pow((PontoX-2),2)
    deltaY = math.pow((PontoY-2),2)
    Distancia_Euclidiana = math.sqrt(deltaX+deltaY)

    if Distancia_Euclidiana < 2: #Conferencia se o ponto está dentro do raio
        Pontos_no_Circulo = Pontos_no_Circulo+1
    init = init+1

Valor_de_Pi = 4*(float(Pontos_no_Circulo))/(float(Pontos_no_Quadrado))
print("Valor do ponto X gerado foi de aproximadamente %.3f" %PontoX)
print("Valor do ponto Y gerado foi de aproximadamente %.3f" %PontoY)
print ("Cateto de X e aproximadamente %.3f" %deltaX)
print ("Cateto de Y e aproximadamente %.3f" %deltaY)
print ("O valor da distancia Euclidiana e aproximadamente %.3f" %Distancia_Euclidiana)

print ("O valor de pi e aproximadamente %.3f" %Valor_de_Pi)

