palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis')
for palavra in palavras:
    print(f'\nNa palavras {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
