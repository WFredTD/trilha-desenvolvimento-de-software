import functools


def log_chamada(func):
    """
    Um decorador que registra (loga) a chamada de uma função.

    Imprime o nome da função e todos os argumentos (posicionais e nomeados)
    passados para ela antes de executar a função original.

    Args:
        func (callable): A função a ser decorada.

    Returns:
        callable: A função 'wrapper' que adiciona a funcionalidade de log.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Chamando função '{func.__name__}' com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        return resultado

    return wrapper


@log_chamada
def saudar(nome):
    """
    Retorna uma saudação personalizada.

    Args:
        nome (str): O nome da pessoa a ser saudada.

    Returns:
        str: Uma string de saudação no formato "Olá, [nome]! Bem-vindo ao meu módulo."
    """
    return f"Olá, {nome}! Bem-vindo ao meu módulo."


@log_chamada
def calcular_potencia(base, expoente):
    """
    Calcula a potência de uma base elevada a um expoente.

    Args:
        base (float ou int): O número base.
        expoente (float ou int): O expoente.

    Returns:
        float ou int: O resultado da base elevada ao expoente.
    """
    return base**expoente


@log_chamada
def dividir_numeros(dividendo, divisor):
    """
    Realiza a divisão de dois números.

    Args:
        dividendo (float ou int): O número a ser dividido.
        divisor (float ou int): O número pelo qual dividir.

    Returns:
        float: O resultado da divisão.

    Raises:
        ValueError: Se o divisor for zero.
    """
    if divisor == 0:
        raise ValueError("Não é possível dividir por zero.")
    return dividendo / divisor


if __name__ == "__main__":
    print("--- Demonstrando as funções decoradas ---")

    # Exemplo de chamada da função saudar
    saudacao_result = saudar("Alice")
    print(f"Resultado de saudar: {saudacao_result}\n")

    # Exemplo de chamada da função calcular_potencia
    potencia_result = calcular_potencia(base=3, expoente=4)
    print(f"Resultado de calcular_potencia: {potencia_result}\n")

    # Exemplo de chamada da função dividir_numeros (válida)
    divisao_valida_result = dividir_numeros(dividendo=100, divisor=5)
    print(f"Resultado de dividir_numeros (válida): {divisao_valida_result}\n")

    # Exemplo de chamada da função dividir_numeros (com erro para ver o log e a exceção)
    try:
        divisao_erro_result = dividir_numeros(dividendo=10, divisor=0)
        print(f"Resultado de dividir_numeros (erro): {divisao_erro_result}\n")
    except ValueError as e:
        print(f"Erro esperado capturado ao dividir por zero: {e}\n")

    print("--- Demonstração concluída ---")
