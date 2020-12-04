from time import sleep
input('Precione qualquer tecla para iniciar a contagem regressiva!')
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('\033[7;30m \033[m'*20)
print('{:^20}'.format('\033[7;30m  Feliz ano novo!!! \033[m'))
print('\033[7;30m \033[m'*20)
