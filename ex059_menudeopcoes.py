n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
i: int = 0
while i != 5:
    i = int(input('''Escolha uma opção
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    >>>>>Qual a sua opção? '''))
    if i == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif i == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif i == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif i == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif i > 5:
        print('Opção errada, tente novamente!')
    print('-='*20)
print(' FIM ')
