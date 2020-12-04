from random import randint
num = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print(f'Os números sorteados fora {num[:]}')
menor = maior = num[0]
for i in range(0, 5):
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]
print(f'O menor número sorteado foi {menor} e o maior foi {maior}.')
#  Forma simplificada de fazer o programa:

num = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print(f'\nOs números sorteados fora {num}')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
