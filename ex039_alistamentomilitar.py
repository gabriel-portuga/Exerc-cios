from datetime import date
print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)

anoNascimento = int(input('Ano de nascimento: '))
idadeAtual = date.today().year - anoNascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(anoNascimento, idadeAtual, date.today().year))
if idadeAtual < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idadeAtual))
    print('Seu alistamento será em {}.'.format((18 - idadeAtual) + date.today().year))
elif idadeAtual > 18:
    print('Estamos em {} e você deveria ter se alistado em {}.'
          ''.format(date.today().year, date.today().year - (idadeAtual - 18)))
else:
    print('Você deve se alistar esse ano!')

""" 
Forma como o Guanabara fez
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = 18 - idade
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(saldo))
"""