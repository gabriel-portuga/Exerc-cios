"""
num = soma = cont = media = maior = menor = i = 0
while i != 1:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    media = float(soma / cont)
    if cont == 1:
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    i = int(input('Digite uma opção \n[ 1 ] Sair \n[ 2 ] Continuar\n'))
print('A média entre os números digitador foi {:.2f}, o maior número é'
      ' {} e o menor número é {}.'.format(media, maior, menor))
"""
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))