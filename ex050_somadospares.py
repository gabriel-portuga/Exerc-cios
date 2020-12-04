soma: int = 0
cont: int = 0
for i in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números pares é: {}'.format(cont, soma))
