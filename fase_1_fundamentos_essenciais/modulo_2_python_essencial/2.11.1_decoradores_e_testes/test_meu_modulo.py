import unittest

from meu_modulo import calcular_potencia, dividir_numeros, saudar


class TesteMeuModulo(unittest.TestCase):

    def test_saudar_com_nome_personalizado(self):
        """
        Verifica se a função 'saudar' retorna a saudação correta para um nome específico.
        """
        self.assertEqual(saudar("Fred"), "Olá, Fred! Bem-vindo ao meu módulo.")

    def test_calcular_potencia_de_dois_numeros(self):
        """
        Verifica se a função 'calcular_potencia' calcula corretamente a potência.
        Testa diferentes bases e expoentes.
        """
        self.assertEqual(calcular_potencia(2, 3), 8)
        self.assertEqual(calcular_potencia(5, 2), 25)

    def test_dividir_numeros_validos(self):
        """
        Verifica se a função 'dividir_numeros' realiza divisões corretas.
        Inclui teste com números inteiros e um teste com float para precisão.
        """
        self.assertEqual(dividir_numeros(10, 2), 5)
        self.assertAlmostEqual(dividir_numeros(10, 3), 3.333333, places=6)

    def test_dividir_por_zero_levanta_erro(self):
        """
        Verifica se a função 'dividir_numeros' levanta a exceção ValueError
        quando a tentativa é de dividir por zero.
        """
        with self.assertRaises(ValueError):
            dividir_numeros(10, 0)


if __name__ == "__main__":
    unittest.main()
