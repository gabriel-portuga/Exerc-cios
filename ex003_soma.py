# Tipo primitivos | int() , float(), bool() e str() consecutivamente, inteiro, flutuante, booleano e caractere.
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
s = n1 + n2
print('A soma vale {}' .format(s))

# Modo correto de somar é convertendo a variavel para um tipo primitivo
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {}, vale {}'.format(n1,n2,s))

# int = 7 | -4 | 0 |9875
# float =  4.5 | 0.076 | -15.233 | 7.0
# bool = True | False
# str = 'Olá' | '7.5' | ''

n1 = input('Digite um valor: ')
print(type(n1)) # registra como string pois não foi especificado qual tipo primitivo ser usado.


