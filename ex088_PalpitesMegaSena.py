from random import randint
from time import sleep

# ERRADA POIS PODE REPETIR NÚMEROS NO RANDOM

numeros = []
jogo = []
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
qnt = int(input('Quantos jogos serão criados? '))

print(f'-=-= SORTEANDO {qnt} JOGOS -=-=')
for c in range(0, qnt):
    for i in range(0, 6):
        numeros.append(randint(1, 60))
        jogo.append(numeros[:])
        numeros.clear()
    jogo.sort()
    print(f'Jogo {c+1}: {jogo}')
    jogo.clear()
    sleep(1)
print('Boa sorte!!!')

# CERTO

lista = list()
jogos = list()
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*3, f' SORTEANDO {quant} JOGOS ', '-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
