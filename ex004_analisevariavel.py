teste = input('Digite algo: ')
#if teste.isnumeric() == True:
#   teste = int(teste)
print('O tipo primitivo desse valor é {}'.format(type(teste)))
if teste.isspace() == True:
    print('O valor digitado são apenas espaços')
else: print('O valor digitado não são apenas espaços')
if teste.isnumeric() == True:
    print('O valor digitado contem apenas números')
else: print('O valor digitado não são apenas números')
