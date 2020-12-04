import math
cOposto = float(input('Comprimento do cateto oposto: '))
cAdjacente = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(cOposto, cAdjacente)))

# OU

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))

# OU

cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
hip = (cop ** 2 + cad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
