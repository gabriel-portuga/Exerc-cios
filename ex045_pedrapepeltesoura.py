from random import randint
from time import sleep
print('Vamos jogar \033[34mJOKENPÔ\033[m?')
i: int = 1
itens = ('', 'Pedra', 'Papel', 'Tesoura')
while i == 1:
    jogador = int(input('Escolha uma opcão:\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\nQual é a sua jogada? '))
    computador = randint(1, 3)
    resultado = 'Invalido'
    if jogador == 1:
        if computador == 1:
            resultado = 'EMPATE'
        elif computador == 2:
            resultado = 'Eu GANHEI :)'
        elif computador == 3:
            resultado = 'Você GANHOU :/'
    elif jogador == 2:
        if computador == 1:
            resultado = 'Você GANHOU :/'
        elif computador == 2:
            resultado = 'EMPATE'
        elif computador == 3:
            resultado = 'Eu GANHEI :)'
    elif jogador == 3:
        if computador == 1:
            resultado = 'Eu GANHEI :)'
        elif computador == 2:
            resultado = 'Você GANHOU :/'
        elif computador == 3:
            resultado = 'EMPATE'
    else:
        print('Opção invalida!')
    if jogador == 1 or jogador == 2 or jogador == 3:
     print('JO', end='')
     sleep(1)
     print('KEN', end='')
     sleep(1)
     print('PÔ')
     print('Eu escolhi {} e você escolheu {}, {}'.format(itens[computador], itens[jogador], resultado))
    i = int(input('Deseja jogar novamente? \n[ \033[35m1\033[m ] Jogar \n[ \033[35m2\033[m ] Sair\n'))
    if i >= 3:
        i = 1
print('\033[7;30m Obrigado por usar um APP Go!Sys \033[m')
