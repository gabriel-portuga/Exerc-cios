maior: float = 0
menor: float = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(i)))
    if i == 1:
        menor = peso
    if maior < peso:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {:.1f}kg e o menor {:.1f}kg'.format(maior, menor))
