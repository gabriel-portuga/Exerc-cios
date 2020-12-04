print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[31mREPROVADO\033[m!')
elif media < 7:
    print('\033[33mRECUPERAÇÃO\033[m!')
elif media <= 10:
    print('\033[34mAPROVADO\033[m!')
else:
    print('ERRO!')
