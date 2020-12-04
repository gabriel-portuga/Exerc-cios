from datetime import date  # Na biblioteca datetime importamos o Date para coletar a data
ano = int(input('Que ano quer analisar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year  # pega a data de hj e o .year pega apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
