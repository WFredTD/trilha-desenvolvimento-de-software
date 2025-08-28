class ProcessadorDeArquivos:
    """
    Classe com métodos para processar arquivos de texto.
    """

    def __init__(self):
        pass

    def processar_e_salvar(self, arquivo_entrada, arquivo_saida):
        """
        Lê o conteúdo de um arquivo, converte o texto para maiúsculas
        e salva o resultado em um novo arquivo.

        Args:
            arquivo_entrada (str): O caminho para o arquivo de entrada.
            arquivo_saida (str): O caminho para o arquivo de saída.
        """

        try:
            with open(arquivo_entrada, "r", encoding="utf-8") as f_entrada:
                arquivo_lido = f_entrada.read()
                conteudo_modificado = arquivo_lido.upper()
            with open(arquivo_saida, "w", encoding="utf-8") as f_saida:
                f_saida.write(conteudo_modificado)

        except FileNotFoundError as e:
            print(f"Erro: O arquivo de entrada não foi encontrado: {e}")
            raise

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            raise

        finally:
            print("Processamento concluído.")


if __name__ == "__main__":
    # Cria uma instância da classe
    processador = ProcessadorDeArquivos()

    # Chama a função, passando 'dados.txt' como argumento para o parâmetro 'arquivo_entrada'
    processador.processar_e_salvar("dados.txt", "resultado.txt")
