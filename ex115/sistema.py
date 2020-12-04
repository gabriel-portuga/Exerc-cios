from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoa', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Criar Aquivo')
        if not arquivoExiste(arq):
            criarArquivo(arq)
        else:
            print('Arquivo já existente!')
    elif resposta == 2:
        cabecalho('Cadastrar Pessoa')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Listar Pessoas')
        lerArquivo(arq)
    elif resposta == 4:
        sair()
        break
    else:
        print('Opção inválida, tente novamente...')
    sleep(1)
