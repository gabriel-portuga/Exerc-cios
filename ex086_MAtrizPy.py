matriz = [[], [], []]
"""for c in range(0, 3):
    matriz[0].append(int(input(f'Digite o valor da matriz [0,{c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite o valor da matriz [1,{c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite o valor da matriz [2,{c}]: ')))
print(matriz[0])
print(matriz[1])
print(matriz[2])"""

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite o valor da matriz [{lin},{col}]: ')))
print("-="*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
