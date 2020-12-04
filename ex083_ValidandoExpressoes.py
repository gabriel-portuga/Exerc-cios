exp = input('Digite uma expressão: ')
direita = exp.count('(')
esquerda = exp.count(')')
if direita == esquerda:
    print('Sua expressão está correta! ')
else:
    print('Sua expressão está incorreta! ')

# Resolução do Guanabara
expr = input('Digite a exprssão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
