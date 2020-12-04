n1 = float(input('Digite o preço do produto para aplicar o desconto de 5%: R$'))
print('O produto que custava {:.2f} reais saira por apenas {:.2f} reais'.format(n1, n1 - (n1*5/100)))
# Forma mais facil de calcular porcentagem >>> 10 * 5 / 100 == 5% == 0.5 <<<<