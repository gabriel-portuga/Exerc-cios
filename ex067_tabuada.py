while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num < 0:
        break
    print('-'*20)
    for i in range(1, 11):
        print(f'{num} x {i:>2} = {num * i}')
    print('-'*20)
    continua = 's'
    while continua in 'sS':
        continua = str(input('Deseja continua? [S/N] ')).strip().upper()[0]
        if continua in 'sS':
            break
    if continua in 'nN':
        break
