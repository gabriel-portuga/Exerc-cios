""" ERRADO
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
escolha: int = 1
while escolha != 0:
    while cont <= 10:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    escolha = int(input('Deseja mostrar mais quantos termos: '))
    cont = 1
print('FIM')
"""
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont: int = 1
total: int = 0
escolha: int = 10
while escolha != 0:
    total = total + escolha
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    escolha = int(input('Deseja mostrar mais quantos termos: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
