cont: int = 0
n1 = int(input('Digite um número: '))
for i in range(1, n1+1):
    if n1 % i == 0:
        print('\033[33m{}\033[m'.format(i), end=' ')
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
if cont == 2:
    print('\nO número {} foi divisível {} vezes\nE por isso ele É PRIMO!'.format(n1, cont))
else:
    print('\nO número {} foi divisível {} vezes \nE por isso ele NÃO Ë PRIMO!'.format(n1, cont))
