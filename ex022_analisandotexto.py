print('Seja bem vindo!')
nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiusculo é: ', nome.upper())
print('Seu nome em minusculo é: ', nome.lower())

# semEspaco = nome.count(' ')
# comEspaco = len(nome)
# total = comEspaco - semEspaco
# print('Seu nome tem {} letras ao todo'.format(total))

print('Seu nome tem ao todo {} letras sem espaços'.format(len(nome) - nome.count(' ')))
nomeSeparado = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nomeSeparado[0])))
