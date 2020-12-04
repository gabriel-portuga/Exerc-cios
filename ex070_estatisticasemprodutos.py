"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print('-'*20)
print('{:^20}'.format('LOJA DOS SILVA'))
print('-'*20)
total = precobarato = produtocaro = 0
nomebarato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    if total == 0:
        precobarato = preco
        nomebarato = produto
    total += preco
    if precobarato > preco:
        precobarato = preco
        nomebarato = str(produto)
    if preco > 1000:
        produtocaro += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^21}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtocaro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${precobarato:.2f}')
