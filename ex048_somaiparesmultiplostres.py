soma: int = 0
cont: int = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))