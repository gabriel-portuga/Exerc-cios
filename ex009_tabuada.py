n1 = int(input('Digite um valor para exibir sua tabuada: '))
i = 1
print('-'*12)
while i<11:
    print('{} x {:2} = {}'.format(n1, i, n1*i))
    i = i+1
print('-'*12)