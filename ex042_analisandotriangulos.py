print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)

print('-='*20)
print('   Analisador de triângulos:')
print('-='*20)
n1 = int(input('Digite o valor de uma reta: '))
n2 = int(input('Digite o valor de outra reta: '))
n3 = int(input('Digite o valor da ultima reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 and n2 == n3:  # Pode se usar n1 == n2 == n3
        triangulo = 'Equilátero'
    elif n1 == n2 or n2 == n3:
        triangulo = 'Isósceles'
    else:
        triangulo = 'Escaleno'
    print('Pode formar um triangulo {}.'.format(triangulo))
else:
    print('Não pode formar um triangulo')
