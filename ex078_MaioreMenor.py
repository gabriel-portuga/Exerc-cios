numeros = list()
maior = menor = 0
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição({i}): ')))
    if i == 0:
        maior = menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print('=-'*30)
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posiçoes ', end='')
for i, v in enumerate(numeros):
    if numeros[i] == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(numeros)} nas posiçoes ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print()
