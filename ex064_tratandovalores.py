"""num: int = 0
cont: int = 0
soma: int = 0"""
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número[999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Foram digitador {} números e a soma entre eles é: {}.'
      ''. format(cont, soma))
