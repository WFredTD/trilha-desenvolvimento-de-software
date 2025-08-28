class ManipuladorDeDados:
    def __init__(self):
        pass

    def contar_frequencia(self, lista_elementos):
        """
        Conta a frequência de cada elemento em uma lista.

        Args:
            lista_elementos (list): Lista de elementos a serem contados.

        Returns:
            dict: Dicionário com a frequência de cada elemento.
        """
        frequencia = {}
        for i in lista_elementos:
            # O get(i, 0) retorna o valor de 'i' ou 0 se 'i' não existir no dicionário
            frequencia[i] = frequencia.get(i, 0) + 1
        return frequencia

    def encontrar_duplicatas(self, lista_elementos):
        """
        Encontra elementos duplicados em uma lista.

        Args:
            lista_elementos (list): Lista de elementos a serem verificados.

        Returns:
            list: Lista de elementos duplicados sem repetição.
        """
        duplos = []
        lista = []
        for i in lista_elementos:
            if i in lista and i not in duplos:
                duplos.append(i)
            else:
                lista.append(i)
        return duplos

    def combinar_dados(self, dados1, dados2):
        """
        Combina dois dicionários em um único. Caso os dicionários tenham chaves duplicadas, o último tem preferência.

        Args:
            dados1 (dict): Primeiro dicionário.
            dados2 (dict): Segundo dicionário.

        Returns:
            dict: Dicionário combinado.
        """
        # O operador | combina os dicionários, e o último tem preferência em caso de chaves duplicadas.
        return dados1 | dados2


if __name__ == "__main__":
    # Cria uma instância da classe ManipuladorDeDados
    manipulador = ManipuladorDeDados()

    # --- Demonstração do método contar_frequencia ---
    print("\n--- Demonstração: Contagem de Frequência ---")
    lista_frequencia = [1, 2, 2, 3, 1, 4, 1]
    frequencia = manipulador.contar_frequencia(lista_frequencia)
    print(f"Lista original: {lista_frequencia}")
    print(f"Frequência dos elementos: {frequencia}")
    print("-" * 40)

    # --- Demonstração do método encontrar_duplicatas ---
    print("\n--- Demonstração: Encontrar Duplicatas ---")
    lista_duplicatas = [1, 2, 3, 2, 3, 3, 4, 5, 4, 5, 3, 6]
    duplicatas = manipulador.encontrar_duplicatas(lista_duplicatas)
    duplicatas.sort()
    print(f"Lista original: {lista_duplicatas}")
    print(f"Elementos duplicados: {duplicatas}")
    print("-" * 40)

    # --- Demonstração do método combinar_dados ---
    print("\n--- Demonstração: Combinação de Dicionários ---")
    dados1 = {"nome": "Walter", "idade": 30}
    dados2 = {"cidade": "Brasília", "idade": 35}
    dicionario_combinado = manipulador.combinar_dados(dados1, dados2)
    print(f"Primeiro dicionário: {dados1}")
    print(f"Segundo dicionário: {dados2}")
    print(f"Dicionário combinado: {dicionario_combinado}")
    print("-" * 40)
