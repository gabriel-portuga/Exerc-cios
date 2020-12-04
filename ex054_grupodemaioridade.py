from datetime import date
maior: int = 0
menor: int = 0
for i in range(1, 8):
    nasc = int(input('Qual o ano do seu nascimento? '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print('Das 7 pessoas digitadas, {} são menores e {} já são maiores'.format(menor, maior))
