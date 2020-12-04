velocidade = float(input('Qual a velocidade do carro na via? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você execeu o limite permetido que é de 80Km/h \n'
          'Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
