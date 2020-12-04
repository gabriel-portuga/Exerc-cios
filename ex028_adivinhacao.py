from random import randint  # Importa apenas o Randint da biblioteca Random
from time import sleep  #  Essa função faz com que o computar espere para continuar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
computador = randint(0, 5)  # escolhe um valor entre 0 e 5 automaticamente
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)  # Pausa o programa por 3 segundos
if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu! Eu pensei no número {} e você no {}.'.format(computador, jogador))
print('--FIM--')
