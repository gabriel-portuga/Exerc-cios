def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preco invalido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: ')).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! {n} não é um valor válido. Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
