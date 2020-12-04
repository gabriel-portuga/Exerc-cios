def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        else:
            return n2


num = leiaint('Digite um valor INTEIRO: ')
num2 = leiafloat('Digite um valor REAL: ')
print(f'Os valor digitados foram {num}, {num2:.1f}')
