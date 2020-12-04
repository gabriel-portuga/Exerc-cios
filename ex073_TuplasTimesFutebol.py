tabbrasileirao = ('Flamengo', 'Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Santos', 'Grêmio',
                  'Fluminense', 'Athletico-PR', 'Bahia', 'Bragantino', 'Sport Recife', 'Fortaleza', 'Corinthians',
                  'Ceará SC', 'Atlético-GO', 'Vasco da Gama', 'Coritiba', 'Botafogo', 'Goiás')
print('A) ', tabbrasileirao[:5])  # Para mostrar um embaixo do outro podemos usar o for
# for i in tabbrasileirao:
#   print(tabbrasileirao[i])
print('-'*len(tabbrasileirao))
print('B) ', tabbrasileirao[-4:])
print('-'*len(tabbrasileirao))
print('C) ', sorted(tabbrasileirao))
print(tabbrasileirao.index('Flamengo')+1)
