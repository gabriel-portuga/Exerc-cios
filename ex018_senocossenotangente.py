import math
ang = float(input('Digite o angulo que você deseja: '))
# temos que converter para radiano para calcular corretamente
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, math.tan(math.radians(ang))))

# OU  de uma forma mais leve

from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que você deseja: '))
# temos que converter para radiano para calcular corretamente
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))
