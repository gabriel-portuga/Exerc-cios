"""  Meu programa com erro
frase = str(input('Digite uma frase: ')).strip()
frase2 = [len(frase)]
for i in range(0, len(frase)):
    frase2[i] = frase[(len(frase)-(i+1)):(len(frase)-i)]
    print(frase2)
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # igual o for, imprimir a palavra ao contrario
"""inverso = ''
for letra in range(len(junto) - 1, -1, -1):  # Começa em numero de letras de junto -1, vai até o final -1, invertido
    inverso += junto[letra]"""
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
