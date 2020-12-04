print('-='*20)
print('   Analisador de triângulos:')
print('-='*20)
n1 = int(input('Digite o valor de uma reta: '))
n2 = int(input('Digite o valor de outra reta: '))
n3 = int(input('Digite o valor da ultima reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')
