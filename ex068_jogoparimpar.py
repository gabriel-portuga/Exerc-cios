"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
cont = stop = 0
while True:
    num = int(input('Digite um valor: '))
    jogador = ' '
    while jogador not in 'IP':
        jogador = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    computador = randint(0, 10)
    if jogador in 'pP':
        if ((num + computador) % 2) == 0:
            print('Você Ganhou')
            cont += 1
        else:
            print(f'Você jogou {num} e o computador jogou {computador}, o total deu {num + computador} IMPAR')
            stop = 1
    if jogador in 'Ii':
        if ((num + computador) % 2) != 0:
            print('Você Ganhou!')
            cont += 1
        else:
            print(f'Você jogou {num} e o computador jogou {computador}, o total deu {num + computador} PAR')
            stop = 1
    if stop == 1:
        break
print(f'GAME OVER! Você venceu {cont} rodadas')
