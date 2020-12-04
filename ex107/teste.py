import moeda

p1 = float(input('Digite um preço: R$'))
print(f'A metaade de R${p1} é R${moeda.metade(p1)}')
print(f'O dobro de R${p1} é R${moeda.dobro(p1)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p1, 10)}')
print(f'Dimiuindo 18%, temos R${moeda.diminuir(p1, 18)}')
