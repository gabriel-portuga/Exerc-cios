sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]  # o [0] faz com que pegue somente a 1 letra digitada
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. tente novamente\nSexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
