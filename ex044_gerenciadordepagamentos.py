preco1 = float(input('Digite o valor do produto desejado: R$'))
print('''Formas de pagamento:
(\033[7;30m1\033[m) À vista dinheiro / cheque: 10% de desconto
(\033[7;30m2\033[m) À vista no cartão: 5% de desconto
(\033[7;30m3\033[m) Em ate 2x no cartão sem juros
(\033[7;30m4\033[m)Em 3x ou mais no cartão com juros de 20%
''')
pagamento = int(input('Qual a opção desejada? '))
if pagamento == 1:
    preco2: float = preco1 - (preco1 * 10 /100)
elif pagamento == 2:
    preco2: float = preco1 - (preco1 * 5 / 100)
elif pagamento == 3:
    preco2: float = preco1
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco2: float = preco1 + (preco1 * 20 / 100)
    print('Sua compra será parcelada em {}x de {} \033[31mcom juros\033[m'.format(parcelas, (preco2 / parcelas)))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco1, preco2))
