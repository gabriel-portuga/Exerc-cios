num = []
par = []
impar = []
for i in range(0, 7):
    num.append(int(input(f'Digite o {i+1}° número: ')))
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])
print(f'Digitados: {num} \nPares: {sorted(par)} \nImpares: {sorted(impar)}')
# Forma com 3 listas do Guanabara

núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print(f'Todos os valores: {núm}')
núm[0].sort()
print(f'Os valores pares digitados fora: {núm[0]}')
núm[1].sort()
print(f'Os valores ímpares digitados foram: {núm[1]}')
