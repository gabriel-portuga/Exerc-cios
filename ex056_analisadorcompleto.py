nomevelho: str = ''
maisvelho: int = 0
mediaidade: float = 0
qntmulheresmenor: int = 0
for i in range(1, 5):
    nome = str(input('Nome da {} pessoa: '.format(i))).strip().title()
    idade = int(input('Idade da {} pessoa: '.format(i)))
    sexo = str(input('Sexo da {} pessoa (F/M): '.format(i))).strip().upper()
    mediaidade = mediaidade + idade
    if idade > maisvelho and sexo[0] == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo[0] == 'F' and idade < 20:
        qntmulheresmenor += 1
mediaidade = mediaidade / 4
print('A média de idade do grupo é {:.1f}.'.format(mediaidade))
print('O nome do homen mais velho é {}.'.format(nomevelho).title())
print('{} mulheres têm menos de 20 anos.'.format(qntmulheresmenor))
