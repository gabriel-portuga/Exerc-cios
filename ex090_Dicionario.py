"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 6:
    aluno['situacao'] = str('Reprovado')
else:
    aluno['situacao'] = str('Aprovado')
print('=-'*20)
""" print(f' - nome é igual a {aluno["nome"]}')
    print(f' - média é igual a {aluno["media"]}')
    # print(' - situação é igual a Recuperação') if aluno['media'] < 6 else print(' - situação é igual a Aprovado')
    print(f' - situação é igual a {aluno["situacao"]}')
"""
for k, v in aluno.items():  # Para cada KEY(chave, indice), no VALUE(valor, elemento), dentro de aluno(dicionário)
    print(f'{k} é igual a {v}')
