import re


class ProcessadorDeDados:
    def __init__(self):
        pass

    def validar_email(self, email):
        """
        Valida se uma string é um endereço de e-mail válido, seguindo um padrão básico.

        Args:
            email (str): O e-mail a ser validado.

        Returns:
            bool: True se o e-mail for válido, False caso contrário.
        """
        padrao = r"^[A-Za-z0-9._%+]+@[A-Za-z0-9-]+(\.[a-zA-Z]{2,})+$"
        return bool(re.match(padrao, email))

    def extrair_urls(self, texto):
        """
        Utiliza expressões regulares para encontrar todas as URLs que começam com http:// ou https:// em um texto.
        Caso nenhuma URL for encontrada, retorna uma lista vazia.

        Args:
            Texto (str): O texto a ser processado.

        Returns:
            list: Lista com todas as URLs encontradas.
        """
        # Padrão RegEx simples que captura qualquer URL que comece com http/https
        # e tenha uma sequência de caracteres não-espaço.
        padrao = r"https?://\S+"

        # Encontra todas as URLs que correspondem ao padrão
        urls_encontradas = re.findall(padrao, texto)

        # Limpa a pontuação indesejada do final de cada URL encontrada.
        urls_limpas = []
        for url in urls_encontradas:
            urls_limpas.append(url.strip(".,!?;"))

        return urls_limpas

    def formatar_texto(self, texto):
        """
        Utiliza expressões regulares para:
            Remover espaços múltiplos, substituindo-os por um único espaço.
            Remover caracteres especiais (por exemplo, `!`, `@`, `#`, `$` etc.), mas mantendo letras, números e espaços.

        Args:
            Texto (str): O texto a ser processado.

        Returns:
            str: Texto formatado.
        """
        # 1. Substitui espaços múltiplos por um único espaço
        texto_formatado = re.sub(r"\s+", " ", texto)

        # 2. Remove caracteres especiais
        texto_final = re.sub(r"[^a-zA-Z0-9 ]", "", texto_formatado)

        return texto_final


if __name__ == "__main__":
    # Cria uma instância da classe ProcessadorDeDados
    processador = ProcessadorDeDados()

    # --- Demonstração do método validar_email ---
    print("\n--- Demonstração: Validação de E-mails ---")
    email_valido = "usuario.exemplo@dominio.com.br"
    email_invalido = "usuario@dominio"
    print(f"E-mail '{email_valido}': Válido? {processador.validar_email(email_valido)}")
    print(
        f"E-mail '{email_invalido}': Válido? {processador.validar_email(email_invalido)}"
    )
    print("-" * 45)

    # --- Demonstração do método extrair_urls ---
    print("\n--- Demonstração: Extração de URLs ---")
    texto_com_urls = "Visite nosso site: https://www.exemplo.com. E também nosso blog: http://blog.exemplo.com.br/artigo."
    urls_encontradas = processador.extrair_urls(texto_com_urls)
    print(f"Texto original:\n'{texto_com_urls}'")
    print(f"\nURLs encontradas: {urls_encontradas}")
    print("-" * 45)

    # --- Demonstração do método formatar_texto ---
    print("\n--- Demonstração: Formatação de Texto ---")
    texto_sujo = (
        "Este texto.!!@@@ possui      espacos multiplos e $$caracteres_especiais!"
    )
    texto_formatado = processador.formatar_texto(texto_sujo)
    print(f"Texto original:\n'{texto_sujo}'")
    print(f"\nTexto formatado:\n'{texto_formatado}'")
    print("-" * 45)
