import moeda

p1 = float(input('Digite um preço: R$'))
print(f'A metaade de {moeda.moeda(p1)} é {moeda.moeda(moeda.metade(p1))}')
print(f'O dobro de {moeda.moeda(p1)} é {moeda.moeda(moeda.dobro(p1))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p1, 10))}')
print(f'Dimiuindo 18%, temos {moeda.moeda(moeda.diminuir(p1, 18))}')

print(f'Mostrar em dolar, {moeda.moeda(p1, "US")}')
