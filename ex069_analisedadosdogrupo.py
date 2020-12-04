"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
maior = homens = mmenor = 0
while True:
    print('-'*20)
    print('{:^20}'.format('CADASTRE UMA PESSOA'))
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()
    print('-'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mmenor += 1
print(f'O total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mmenor} mulheres com menos de 20 anos')
