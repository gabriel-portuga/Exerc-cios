frase = input('Digite uma frase: ').strip()
print('A letra A aparece {} vezes na frase: {}.'.format(frase.lower().count('a'), frase))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))  # Diz a posição começando da direita pra E
