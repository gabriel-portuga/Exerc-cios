def escrever(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


# Programa Principal
escrever('Gabriel Silva')
