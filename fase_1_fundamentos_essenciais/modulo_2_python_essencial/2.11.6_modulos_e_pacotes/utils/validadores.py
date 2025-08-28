import re


def eh_par(numb):
    """
    Valida um número par
    Args:
        numb (int): Número a ser validado

    Returns:
        bool: True se o número for par, False caso contrário
    """
    if numb % 2 == 0:
        return True
    else:
        return False


def eh_email_valido(email):
    """
    Valida um endereço de email

    Args:
        email (str): Endereço de email a ser validado

    Returns:
        bool: True se o email for válido, False caso contrário
    """
    padrao = r"^[A-Za-z0-9._%+]+@[A-Za-z0-9-]+(\.[a-zA-Z]{2,})+$"
    return bool(re.match(padrao, email))
