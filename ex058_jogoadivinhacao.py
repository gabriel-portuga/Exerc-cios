from random import randint
from time import sleep
print('Vou pensar em um número')
print('Processando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
computador = randint(0, 10)
jogador = int(input('Qual foi o número que eu pensei? '))
cont: int = 1
while jogador != computador:
    jogador = int(input('Errou, tente novamente: '))
    cont += 1
print('Você precisou de {} tentativas para vencer.'.format(cont))

"""
Código do Guanabara
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez: ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
"""