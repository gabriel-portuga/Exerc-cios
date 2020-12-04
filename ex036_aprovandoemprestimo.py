print('\033[7;30m-=\033[m'*15)
print(' \033[7;30m   Bem vindo ao APP Go!Sys  \033[m')
print('\033[7;30m-=\033[m'*15)
# Inicio do código
imovel = float(input('\nQual o valor do imovel ? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
parcelas = int(input('Em quantos anos de financiamento? '))
prestacao = imovel / (parcelas * 12)
if prestacao <= (salario * 30 / 100):
    situacao = '\033[1;34mAPROVADO\033[m'
else:
    situacao = '\033[1;31mNEGADO\033[m'
print('Para pagar um imovel de R${:.2f} em {} anos, a pretação será de R${:.2f}.'.format(imovel, parcelas, prestacao))
print('Empréstimo {}!'.format(situacao))
