def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa /100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>7.2f}'.replace('.', ',')


def resumo(preco=0, tplus=0, tless=0):
    print('~'*30)
    print('Resumo do valor'.center(30))
    print('~'*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{tplus}% de aumento: \t{aumentar(preco, tplus, True)}')
    print(f'{tless}% de redução: \t{diminuir(preco, tless, True)}')
    print('~'*30)

