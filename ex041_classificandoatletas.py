from datetime import date
print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)

nasc = int(input('Para verificar sua categoria, digite o ano de seu nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JÚNIOR'
elif idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos.\nClassificaçao: {}.'.format(idade, cat))
