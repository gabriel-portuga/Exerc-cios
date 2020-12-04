from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

# No modo tradicional

n1 = int(input('Digite um número para calcular seu Fatorial: '))
c = n1
# fatorial = 1
print('Calculando {}! = '.format(n1), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(factorial(n1)), end='')
    # f *= c
    c -= 1
# print(fatorial)

# Com FOR

n2 = int(input('\nDigite um número para calcular seu Fatorial: '))
i = n2
print('Calculando {}! = '.format(n2), end='')
for i in range(n2, 0, -1):
    print('{} '.format(i), end='')
    print(' x ' if i > 1 else ' = {}'.format(factorial(n2)), end='')
