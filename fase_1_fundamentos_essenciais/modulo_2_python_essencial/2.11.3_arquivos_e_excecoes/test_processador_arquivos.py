import os
import unittest

from processador_arquivos import ProcessadorDeArquivos


class TestProcessadorDeArquivos(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste antes de cada teste.
        """
        # Cria uma instância da classe a ser testada
        self.processador = ProcessadorDeArquivos()

        # Conteúdo inicial do arquivo de entrada
        self.conteudo_inicial = "Este eh um texto de exemplo para o teste."
        self.arquivo_entrada_teste = "teste_entrada.txt"
        self.arquivo_saida_teste = "teste_saida.txt"

        # Cria o arquivo de entrada ANTES do teste
        with open(self.arquivo_entrada_teste, "w") as f:
            f.write(self.conteudo_inicial)

    def tearDown(self):
        """
        Limpa o ambiente de teste após cada teste.
        """
        if os.path.exists(self.arquivo_entrada_teste):
            os.remove(self.arquivo_entrada_teste)
        if os.path.exists(self.arquivo_saida_teste):
            os.remove(self.arquivo_saida_teste)

    def test_lendo_e_escrevendo_em_um_arquivo(self):
        """
        Verifica se o método processar_e_salvar lê e escreve em um arquivo.
        """

        # 1. Chama o método a ser testado
        self.processador.processar_e_salvar(
            self.arquivo_entrada_teste, self.arquivo_saida_teste
        )

        # 2. Abre o arquivo de saída criado pelo método e lê seu conteúdo
        with open(self.arquivo_saida_teste, "r") as f_saida:
            conteudo_saida = f_saida.read()

        # 3. Define o conteúdo esperado (o inicial em maiúsculas)
        conteudo_esperado = self.conteudo_inicial.upper()

        # 4. Faz a asserção para verificar se o conteúdo de saída é o esperado
        self.assertEqual(conteudo_saida, conteudo_esperado)

    def test_lendo_um_arquivo_que_nao_existe(self):
        """
        Verifica se o método processar_e_salvar levanta uma exceção quando o arquivo de entrada não existe.
        """
        with self.assertRaises(FileNotFoundError):
            self.processador.processar_e_salvar(
                "arquivo_que_nao_existe.txt", "saida.txt"
            )


if __name__ == "__main__":
    unittest.main()
