matriz = [[], [], []]
somapar = soma3col = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite o valor da matriz [{linha}/{coluna}]: ')))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if coluna == 2:
            soma3col += matriz[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[\033[31m{matriz[linha][coluna]:^5}\033[m]', end='')
    print()
print(f'A soma de todos os valores pares digitados foi: {somapar}')
print(f'A soma dos valores da terceira coluna foi: {soma3col}')
print(f'O maior valor da segunda linha foi: {max(matriz[1])}')
