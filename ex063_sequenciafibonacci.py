n = int(input('Digite um número: '))
print('Os {} primeiros elementos da sequência de Fibonacci são: '.format(n))
primeiro: int = 0
segundo: int = 1
fibonacci = primeiro + segundo
print('Sequência fibonacci: {} -> {}'.format(primeiro, segundo), end=' ')
for i in range(1, n):
    print('-> {}'.format(fibonacci), end=' ')
    primeiro = segundo
    segundo = fibonacci
    fibonacci = primeiro + segundo
print('\nFIM')
