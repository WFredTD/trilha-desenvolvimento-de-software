import unittest

from utils.cauculos import soma, subtracao
from utils.validadores import eh_email_valido, eh_par


class Testes(unittest.TestCase):
    def setUp(self):
        """
        Método chamado antes de cada teste.
        """
        pass

    def test_soma(self):
        """
        Teste para a função soma com valores inteiros.
        """
        self.assertEqual(soma(1, 2), 3)

    def test_soma_negativos(self):
        """
        Teste para a função soma com valores negativos.
        """
        self.assertEqual(soma(-1, -2), -3)

    def test_soma_float(self):
        """
        Teste para a função soma com valores flutuantes.
        """
        self.assertEqual(soma(1.5, 2.5), 4.0)

    def test_subtracao(self):
        """
        Teste para a função subtracao com valores inteiros.
        """
        self.assertEqual(subtracao(1, 2), -1)

    def test_subtracao_negativos(self):
        """
        Teste para a função subtracao com valores negativos.
        """
        self.assertEqual(subtracao(-1, -2), 1)

    def test_subtracao_float(self):
        """
        Teste para a função subtracao com valores flutuantes.
        """
        self.assertEqual(subtracao(1.5, 2.5), -1.0)

    def test_eh_par(self):
        """
        Teste para a função eh_par com valor par positivo.
        """
        self.assertTrue(eh_par(2))

    def test_eh_par_impar(self):
        """
        Teste para a função eh_par com valor ímpar positivo.
        """
        self.assertFalse(eh_par(3))

    def test_eh_par_negativo(self):
        """
        Teste para a função eh_par com valor ímpar negativo.
        """
        self.assertFalse(eh_par(-1))

    def test_eh_impar_negativo(self):
        """
        Teste para a função eh_par com valor par negativo.
        """
        self.assertTrue(eh_par(-2))

    def test_validar_email_valido(self):
        """
        Teste para a função eh_email_valido com e-mails válidos.
        """
        self.assertTrue(eh_email_valido("teste@exemplo.com"))
        self.assertTrue(eh_email_valido("nome.sobrenome@sub.dominio.com.br"))

    def test_validar_email_invalido(self):
        """
        Teste para a função eh_email_valido com e-mails inválidos.
        """
        self.assertFalse(eh_email_valido("teste@exemplo"))
        self.assertFalse(eh_email_valido("teste.com"))
        self.assertFalse(eh_email_valido("@exemplo.com"))
        self.assertFalse(eh_email_valido("teste@.com"))
        self.assertFalse(eh_email_valido("teste@@teste.com"))


if __name__ == "__main__":
    unittest.main()
