import unittest
from unittest.mock import patch

from biblioteca import Biblioteca, Livro, Revista


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente de teste antes de cada teste.
        """
        self.biblioteca = Biblioteca()

    def test_criacao_livro(self):
        """
        Testa a criação de um objeto Livro.
        """

        # 1. Instancia o objeto Livro com os dados de teste
        titulo_esperado = "Dom Casmurro"
        autor_esperado = "Machado de Assis"
        isbn_esperado = "978-85-12345-67-8"

        livro = Livro(titulo_esperado, autor_esperado, isbn_esperado)

        # 2. Usa os getters para verificar se o objeto foi criado corretamente
        self.assertEqual(livro.get_titulo(), titulo_esperado)
        self.assertEqual(livro.get_autor(), autor_esperado)

        # 3. Verifica o ISBN do objeto.
        self.assertEqual(livro.get_isbn(), isbn_esperado)

    def test_criacao_revista(self):
        """
        Testa a criação de um objeto Revista.
        """

        titulo_esperado = "National Geographic"
        autor_esperado = "Vários"
        edicao_esperada = "Maio 2023"

        revista = Revista(titulo_esperado, autor_esperado, edicao_esperada)

        self.assertEqual(revista.get_titulo(), titulo_esperado)
        self.assertEqual(revista.get_autor(), autor_esperado)

        self.assertEqual(revista.get_edicao(), edicao_esperada)

    def test_adicionar_material_existente_biblioteca(self):
        """
        Verifica se o método adcionar_material cria o acervo da biblioteca corretamente.
        """
        livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-12345-67-8")
        revista = Revista("National Geographic", "Vários", "Maio 2023")

        self.biblioteca.adicionar_material(livro)
        self.biblioteca.adicionar_material(revista)

        # Checa se a lista de materiais tem o tamanho correto
        self.assertEqual(len(self.biblioteca.get_materiais()), 2)

    def test_listar_materiais_chama_exibir_informacoes(self):
        """
        Testa se o método listar_materiais() chama a função print()
        com as saídas corretas, demonstrando o polimorfismo.
        """

        # A instância da classe Biblioteca já é criada no setUp
        livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-12345-67-8")
        revista = Revista("National Geographic", "Vários", "Maio 2023")

        # O 'patch' temporariamente substitui a função 'print' por um mock.
        with patch("builtins.print") as mock_print:
            self.biblioteca.adicionar_material(livro)
            self.biblioteca.adicionar_material(revista)

            # Chama o método que queremos testar. Ele acionará o mock de 'print'.
            self.biblioteca.listar_materiais()

            # Define a lista de chamadas esperadas em ordem.
            chamadas_esperadas = [
                unittest.mock.call("Dom Casmurro adicionado à biblioteca."),
                unittest.mock.call("National Geographic adicionado à biblioteca."),
                unittest.mock.call(livro.exibir_informacoes()),
                unittest.mock.call(revista.exibir_informacoes()),
            ]

            # Verifica se o mock foi chamado com a sequência de chamadas esperada.
            mock_print.assert_has_calls(chamadas_esperadas)

            self.assertEqual(mock_print.call_count, 4)


if __name__ == "__main__":
    unittest.main()
