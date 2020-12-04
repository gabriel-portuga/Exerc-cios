num = []
while True:
    num.append(int(input('Digite um valor: ')))
    escolha = ' '
    while escolha not in 'sSnN':
        escolha = input('Quer continuar ? [S/N] ')
    if escolha in 'Nn':
        break
print(f'Foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi adicionado a lista!')
