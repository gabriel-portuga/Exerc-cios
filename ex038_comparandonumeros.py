print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)
# Inico do condigo
n1 = int(input(('\nDigite um número: ')))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')