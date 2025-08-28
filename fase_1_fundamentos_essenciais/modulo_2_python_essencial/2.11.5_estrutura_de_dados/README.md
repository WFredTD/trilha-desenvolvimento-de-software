💡 Exercício 2.11.5: Estruturas de Dados Essenciais
===================================================

Este diretório contém a solução para o Exercício 2.11.5 da minha Trilha de Desenvolvimento de Software. O objetivo foi reforçar a manipulação de estruturas de dados essenciais em Python, como listas, dicionários e conjuntos, usando o que chamamos de "Python puro" ou "Vanilla Python", sem a necessidade de bibliotecas externas no arquivo principal.

🚀 Tecnologias e Módulos Utilizados
-----------------------------------

-   **Python 3.x**

-   **Módulo `unittest`**: Framework de testes unitários para validar a lógica das funções.

-   **`uv`**: Gerenciador de pacotes e ambientes virtuais.

-   **`black`**: Formatador de código Python.

-   **`isort`**: Ferramenta para organizar imports Python.

✨ Conceitos Abordados
---------------------

-   **Manipulação de Estruturas de Dados:**

    -   **Listas:** Uso de listas como a principal estrutura de dados para armazenar e iterar sobre elementos.

    -   **Dicionários:** Aplicação de dicionários para contar a frequência de elementos de forma eficiente.

- **Operadores Lógicos** O uso de operadores lógicos (and, not in) para construir uma solução elegante e direta para a busca de duplicatas.

-   **Python Puro:** A solução foi implementada utilizando apenas funcionalidades built-in do Python, sem a necessidade de importar módulos extras.

-   **Lógica de Programação:** Desenvolvimento de algoritmos para resolver problemas de forma eficiente, como a busca por duplicatas com uma única passagem (`O(n)`).

-   **Testes de Unidade:** Criação de testes robustos com `unittest` e `assertCountEqual` para validar que o código se comporta como o esperado, independentemente da ordem dos elementos.

📁 Estrutura do Projeto
-----------------------

```
2.11.5_estrutura_de_dados/
├── manipulador_dados.py
├── test_manipulador.py
└── README.md

```

⚙️ Como Executar
----------------

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado e o ambiente virtual ativado.

1.  **Navegue até este diretório:**

    ```
    cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.5_estrutura_de_dados

    ```

2.  **Execute o módulo principal para ver a demonstração da manipulação de dados:**

    ```
    python manipulador_dados.py

    ```

3.  **Execute os testes unitários para validar a implementação:**

    ```
    python -m unittest test_manipulador.py

    ```

    *Você verá o resumo dos testes, indicando se passaram (`OK`).*