nome = str(input("Aluno: ")) 
disciplina = str(input("Disciplina: "))
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3)/3 # Média das 3 notas

if media >= 7.0: 
    print(f"Parabéns, {nome}. Você foi aprovado em {disciplina} com média {media:.2f}")
elif 6.0 < media < 7.0:
    print(f"{nome}, você está de recuperação em {disciplina}. Estude mais para ser aprovado!")
else:
    print(f"{nome}, você está reprovado em {disciplina}.")
