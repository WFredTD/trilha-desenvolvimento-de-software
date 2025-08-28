💡 Exercício 2.11.3: Manipulação de Arquivos e Tratamento de Exceções
=====================================================================

Este diretório contém a solução para o Exercício 2.11.3 da minha Trilha de Desenvolvimento de Software. O objetivo foi praticar a manipulação segura de arquivos em Python e implementar um robusto tratamento de exceções.

🚀 Tecnologias e Módulos Utilizados
-----------------------------------

-   **Python 3.x**

-   **Módulo `os`**: Utilizado para manipular caminhos de arquivos e remover arquivos temporários.

-   **Módulo `unittest`**: Framework de testes unitários para validar o comportamento do código.

-   **`uv`**: Gerenciador de pacotes e ambientes virtuais.

-   **`black`**: Formatador de código Python.

-   **`isort`**: Ferramenta para organizar imports Python.

✨ Conceitos Abordados
---------------------

-   **Manipulação de Arquivos:** Leitura e escrita de arquivos de texto usando os modos `'r'` (read) e `'w'` (write).

-   **Gerenciadores de Contexto (`with open(...)`):** Utilização do bloco `with` para garantir que os arquivos sejam sempre fechados corretamente, mesmo em caso de erros.

-   **Tratamento de Exceções (`try...except...finally`):**

    -   Captura e tratamento de exceções específicas como `FileNotFoundError`.

    -   Uso de um bloco `except` genérico (`Exception`) para capturar erros inesperados.

    -   Uso do bloco `finally` para executar código de limpeza (como mensagens de conclusão), independentemente de o erro ter ocorrido ou não.

-   **Boas Práticas de Código:**

    -   Uso de docstrings e comentários para explicar o propósito de classes e métodos.

    -   Implementação de uma solução robusta para lidar com a codificação de caracteres (`encoding='utf-8'`), evitando erros como `UnicodeEncodeError`.

-   **Testes Unitários (`unittest`):**

    -   Uso dos métodos `setUp` e `tearDown` para preparar e limpar o ambiente de teste (criação e remoção de arquivos temporários).

    -   Verificação de resultados com `assertEqual`.

    -   Validação do tratamento de erros com `self.assertRaises`.

📁 Estrutura do Projeto
-----------------------

```
2.11.3_arquivos_e_excecoes/
├── dados.txt
├── processador_arquivos.py
├── test_processador.py
└── README.md

```

⚙️ Como Executar
----------------

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado e o ambiente virtual ativado, conforme as instruções no [README.md principal](../../../README.md).

1.  **Navegue até este diretório:**

    ```
    cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.3_arquivos_e_excecoes

    ```

2.  **Execute o módulo principal para ver a demonstração da manipulação de arquivos:**

    ```
    python processador_arquivos.py

    ```

    -   Isso criará o arquivo `resultado.txt` e exibirá as mensagens de erro ou sucesso no console.

3.  **Execute os testes unitários:**

    ```
    python -m unittest test_processador.py

    ```

    -   Você verá o resumo dos testes, indicando se passaram (`OK`) ou falharam (`FAILED`).