import unittest

from processador_strings import ProcessadorDeDados


class TestProcessadorDeDados(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste antes de cada teste.
        """
        self.processador = ProcessadorDeDados()

    def test_validar_email_valido(self):
        """
        Verifica se a função validar_email retorna True para e-mails válidos.
        """
        self.assertTrue(self.processador.validar_email("teste@exemplo.com"))
        self.assertTrue(
            self.processador.validar_email("nome.sobrenome@sub.dominio.com.br")
        )

    def test_validar_email_invalido(self):
        """
        Verifica se a função validar_email retorna False para e-mails inválidos.
        """
        self.assertFalse(self.processador.validar_email("teste@exemplo"))
        self.assertFalse(self.processador.validar_email("teste.com"))
        self.assertFalse(self.processador.validar_email("@exemplo.com"))
        self.assertFalse(self.processador.validar_email("teste@.com"))
        self.assertFalse(self.processador.validar_email("teste@@teste.com"))

    def test_extrair_urls(self):
        """
        Verifica se a função extrair_urls extrai corretamente URLs de texto.
        """
        texto_com_urls = "Visite nosso site: https://www.exemplo.com. E também nosso blog: http://blog.exemplo.com.br/artigo."
        urls_esperadas = [
            "https://www.exemplo.com",
            "http://blog.exemplo.com.br/artigo",
        ]
        urls_encontradas = self.processador.extrair_urls(texto_com_urls)
        self.assertEqual(urls_encontradas, urls_esperadas)

    def test_extrais_urls_complexas(self):
        """
        Verifica se a função extrair_urls lida corretamente com URLs complexas.
        """
        texto_complexo = "Para mais informações, acesse o link https://blog.exemplo.com.br/artigo/sobre-ia?utm_source=email&ref=home#comentarios."
        urls_esperadas = [
            "https://blog.exemplo.com.br/artigo/sobre-ia?utm_source=email&ref=home#comentarios"
        ]
        urls_encontradas = self.processador.extrair_urls(texto_complexo)
        self.assertEqual(urls_encontradas, urls_esperadas)

    def test_extrair_urls_sem_urls(self):
        """
        Verifica se a função extrair_urls retorna uma lista vazia para textos sem URLs.
        """
        texto_sem_urls = "Este texto não contém URLs."
        urls_esperadas = []
        urls_encontradas = self.processador.extrair_urls(texto_sem_urls)
        self.assertEqual(urls_encontradas, urls_esperadas)

    def test_formatar_texto_sujo(self):
        """
        Verifica se a função formatar_texto lida corretamente com textos sujos.
        """
        texto_sujo = (
            "Este texto.!!@@@ possui      espacos multiplos e $$caracteres_especiais!"
        )
        texto_esperado = "Este texto possui espacos multiplos e caracteresespeciais"
        texto_formatado = self.processador.formatar_texto(texto_sujo)
        self.assertEqual(texto_formatado, texto_esperado)

    def test_formatar_texto_limpo(self):
        """
        Verifica se a função formatar_texto lida corretamente com textos já formatados.
        """
        texto_limpo = "Este texto ja esta formatado corretamente."
        texto_esperado_limpo = "Este texto ja esta formatado corretamente"
        texto_formatado_limpo = self.processador.formatar_texto(texto_limpo)
        self.assertEqual(texto_formatado_limpo, texto_esperado_limpo)

    def test_formatar_texto_com_um_problema(self):
        """
        Verifica se a função formatar_texto lida corretamente com um problema no texto.
        """
        texto_so_espacos = "Este texto tem       muitos    espacos."
        texto_esperado_so_espacos = "Este texto tem muitos espacos"
        texto_formatado_so_espacos = self.processador.formatar_texto(texto_so_espacos)
        self.assertEqual(texto_formatado_so_espacos, texto_esperado_so_espacos)


if __name__ == "__main__":
    unittest.main()
