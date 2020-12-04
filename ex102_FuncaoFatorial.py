def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O númeroa  a ser calculado
    :param show: (Opcional) Mostra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c> 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa
print(fatorial(5, show=True))
help(fatorial)