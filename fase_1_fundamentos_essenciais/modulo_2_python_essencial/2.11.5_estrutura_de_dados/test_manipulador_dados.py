import unittest

from manipulador_dados import ManipuladorDeDados


class TestManipuladorDados(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente de teste antes de cada teste.
        """
        self.manipulador = ManipuladorDeDados()

    def test_contar_frequencia_lista_simples(self):
        """
        Verifica se a função contar_frequencia retorna um dicionário com as contagens corretas para uma lista simples.
        """

        lista_elementos = [1, 2, 3, 2, 3, 3, 4, 5, 4, 5, 3, 6]
        frequencia_esperada = {1: 1, 2: 2, 3: 4, 4: 2, 5: 2, 6: 1}

        frequencia_encontrada = self.manipulador.contar_frequencia(lista_elementos)

        self.assertEqual(frequencia_esperada, frequencia_encontrada)

    def test_encontrar_duplicatas_lista_com_duplos(self):
        """
        Verifica se a função encontrar_duplicatas retorna uma lista apenas com os elementos duplicados corretamente.
        """

        lista_elementos = [1, 2, 3, 2, 3, 3, 4, 5, 4, 5, 3, 6]
        lista_esperada = [2, 3, 4, 5]

        duplicatas_encontradas = self.manipulador.encontrar_duplicatas(lista_elementos)

        self.assertCountEqual(lista_esperada, duplicatas_encontradas)

    def test_combinar_dados_com_chaves_duplicadas(self):
        """
        Verifica se a função combinar_dados trata corretamente as chaves duplicadas.
        """

        dict1 = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

        dict2 = {
            "escolaridade": "superior cursando",
            "instituição": "Estácio",
            "cidade": "Rio de Janeiro",
        }

        dict_esperado = {
            "nome": "João",
            "idade": 25,
            "cidade": "Rio de Janeiro",
            "escolaridade": "superior cursando",
            "instituição": "Estácio",
        }

        dict_combinado = self.manipulador.combinar_dados(dict1, dict2)

        self.assertEqual(dict_esperado, dict_combinado)


if __name__ == "__main__":
    unittest.main()
