print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)
n = int(input('\nDigite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL'
      '\n[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertendo para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Valor Digitado incorreto, tente novamente!')
