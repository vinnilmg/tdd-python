"""
1 - Recebe um numero inteiro
2 - Verifica se é multiplo de 3 e 5:
    Bacon com ovos
3 - Verifica se o numero é multiplo somente de 3:
    Bacon
4 - Verifica se o numero é multiplo somente de 5:
    Ovos
5 - Verifica se o numero NAO é multiplo de 3 e 5:
    Passa fome
"""


def bacon_com_ovos(num):
    assert isinstance(num, int), 'num deve ser int'

    if num % 3 == 0 and num % 5 == 0:
        return 'Bacon com ovos'

    elif num % 3 == 0:
        return 'Bacon'

    elif num % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
