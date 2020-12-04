import moeda

p1 = float(input('Digite um preço: R$'))
print(f'A metaade de {moeda.moeda(p1)} é {moeda.metade(p1, True)}')
print(f'O dobro de {moeda.moeda(p1)} é {moeda.dobro(p1, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p1, 10, True)}')
print(f'Dimiuindo 18%, temos {moeda.diminuir(p1, 18, True)}')
