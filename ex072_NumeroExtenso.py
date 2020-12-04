extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'douze', 'treze', 'quatorze',
           'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente, Digite um número entre 0 e 20: '))
print(extenso[num])
#  while True:
#   num = int(input('Digite um número entre 0 e 20: '))
#   if 0 <= num <= 20:
#     break
#   print('Tente novamente. ', end='')
#  print(f'Você digitou o número {extenso[num]}')
