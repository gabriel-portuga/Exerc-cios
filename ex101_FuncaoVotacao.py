def voto(ano):
    """
    Serve para retornar a idade atual da pessoa baseado no ano de nascimento
    :param ano:
    :return: Idade
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota!'
    elif idade <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    else:
        return f'Com {idade} anos: Voto Obrigatório!'


# Programa
nasc = int(input('Em que ano vc nasceu? '))
print(voto(nasc))
