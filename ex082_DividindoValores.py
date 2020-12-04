num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    esc = ' '
    while esc not in 'SsNn':
        esc = input('Deseja continuar? [S/N] ').strip().upper()
    if esc in 'Nn':
        break
print(f'Você digitou os seguintes números: {num}')
for i in range(0, len(num)):
    if i % 2 == 0:
        impar.append(num[i])
    else:
        par.append(num[i])
print(f'Os números impares são: {impar}')
print(f'Os números pares são: {par}')
