from time import sleep
num = int(input('Me diga um número qualquer: '))
print('Processando...')
sleep(2)
if num % 2 == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))
