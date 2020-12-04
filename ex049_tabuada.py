i: int = 2
while i == 2:
    n1 = int(input('Digite um número para mostrar sua tabuada: '))
    for j in range(1, 11):
        print('{} x {:>2} = {:>2}'.format(n1, j, n1*j))
    i = int(input('Digite: \n[ 1 ] Sair \n[ 2 ] Calcular outro número\n '))
print('FIM')
