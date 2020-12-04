geral = []
pessoa = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    # if len(geral) == 0:
    #  maipeso = menpeso = 0
    geral.append(pessoa[:])
    pessoa.clear()

    esc = ' '
    while esc not in 'SsNn':
        esc = input('Quer continuar? [S/N] ')
    if esc in 'Nn':
        break
print(f'Ao todo você cadastrou {len(geral)} pessoas.')
maipeso = menpeso = 0

for p in geral:
    if maipeso == 0 and menpeso == 0:
        maipeso = p[1]
        menpeso = p[1]
    elif p[1] > maipeso:
        maipeso = p[1]
    elif p[1] < menpeso:
        menpeso = p[1]
print('--'*20)
print(f'O maior peso foi de {maipeso:.2f}. Os mais pesados foram', end=' ')
for p in geral:
    if p[1] == maipeso:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menpeso:.2f}. Os mais leves foram', end=' ')
for p in geral:
    if p[1] == menpeso:
        print(f'{p[0]}', end=' ')
print('--'*20)
