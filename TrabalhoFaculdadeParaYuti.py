# Função
def parOUimpar(n1):
    """
    -> Função que realiza o teste do valor digitado se é Par ou Impar
    :param n1: Valor que vai ser testado
    :return: Par ou Impar
    """
    if n1 % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


# Programa principal
print('Bem vindo ao somador de números pares!')
numInicial = int(input('Digite um número inteiro para iniciar a contagem: '))
while True:
    numFinal = int(input('Digite um número inteiro para finalizar a contagem: '))
    if numFinal <= numInicial:
        print('Número final deve ser maior que o número inicial!')
    else:
        break
cont = 0
for i in range(numInicial, numFinal+1):
    status = parOUimpar(i)
    print(f'O número {i} é {status}!')
    if status == 'Par':
        cont += 1
print(f'Foram encontrados {cont} números pares no intervalo entre {numInicial} e {numFinal}')
