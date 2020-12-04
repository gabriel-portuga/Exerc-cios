numeros = list()
# Estrutura de repetição infinita
while True:
    n = int(input('Digite um valor: '))
# Estrutura de escolha para adicionar ou não o valor digitado
    if n in numeros:
        print('Valor duplicado! Não irei adiciona-lo')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
# Estrutura de tratamento de escolha para continuar o programa
    escolha = ' '
    while escolha not in 'sSnN':
        escolha = input('Quer continuar ? [S/N] ')
    if escolha in 'Nn':
        break
# Fim do programa
print(sorted(numeros))
