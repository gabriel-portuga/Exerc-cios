import random
i = int(1)
aluno = list(range(4))
for i in range(0, 4):
    aluno[i] = input('Digite o nome do aluno {}: '.format(i+1))
#   print(aluno[i], i)
sorteado = random.randint(0, 3)
print(aluno[sorteado])

# OU

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

# OU mais limpo

i = int(1)
aluno = list(range(4))
for i in range(0, 4):
    aluno[i] = input('Qual o nome do aluno {}: '.format(i+1))
#lista = [aluno[1], aluno[2], aluno[3, aluno[4]]]
escolhido = random.choice(aluno)
print('O aluno escolhido foi {}.'.format(escolhido))
