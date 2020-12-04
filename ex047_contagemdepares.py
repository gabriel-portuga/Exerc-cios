print('Números pares: \n', end='')
s: int = 0
for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=' ')
        s += i
print('\nSoma dos pares: {}\nFIM'.format(s))

# Simplificado

for i in range(2, 51, 2):
    print(i, end=' ')
print('\nFIM')
