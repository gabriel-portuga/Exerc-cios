dias = int(input('Quantos dias foram contratados: '))
km = float(input('Qual a kilometragem rodada com o carro: '))
custoDias = dias * 60
custokm = km * 0.15
print('Foram rodados {:.1f}Km em {} dias e o custo ficou em R${:.2f}'.format(km, dias, custokm + custoDias))
