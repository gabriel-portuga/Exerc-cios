salario = float(input('Qual é o salario do funcionário? R$'))
if salario > 1250:
    salario = salario * 10 / 100 + salario
else:
    salario = salario * 15 / 100 + salario
print('Novo salário {:.2f}'.format(salario))
