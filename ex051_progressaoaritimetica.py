print('='*30)
print('{:^30}'.format('10 termos de uma pa').upper())
print('='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{} '.format(i), end='-> ')
print('ACABOU')
