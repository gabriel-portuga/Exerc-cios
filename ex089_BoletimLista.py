# Código com erro, inacabado!
"""alunos = []
nomes = []
notas = []
medias = []
media = 0
while True:
    nomes.append(input('Nome: '))
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    alunos.append(nomes[:])
    alunos.append(notas[:])
    media = (notas[0] + notas[1]) / 2
    medias.append(media)
    nomes.clear()
    notas.clear()

    esc = ' '
    while esc not in 'SnNn':
        esc = input('Deseja continuar: [S/N]').strip().upper()
    if esc in 'Nn':
        break
print('=-='*0)
print('No.     Nome     Média')
print('=-='*20)
print(medias)"""

# Código correto
ficha = []
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], med])
    esc = ' '
    while esc not in 'SnNn':
        esc = input('Deseja continuar: [S/N]').strip().upper()
    if esc in 'Nn':
        break
print('=-='*10)
print(f'{"No.":<4}{"NOME":10}{"MéDIA":>8}')
print('=-='*10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*20)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
