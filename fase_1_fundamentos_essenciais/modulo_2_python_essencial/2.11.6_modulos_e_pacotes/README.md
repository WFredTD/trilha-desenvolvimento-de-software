💡 Exercício 2.11.6: Módulos e Pacotes
======================================

Este diretório contém a solução para o último exercício do Módulo 2. O objetivo foi praticar a organização de código em pacotes e módulos, uma habilidade fundamental para a construção de projetos grandes e profissionais em Python.

🚀 Tecnologias e Módulos Utilizados
-----------------------------------

-   **Python 3.x**

-   **Módulo `unittest`**: Framework de testes unitários para validar as funções nos módulos.

-   **`uv`**: Gerenciador de pacotes e ambientes virtuais.

-   **`black`**: Formatador de código Python.

-   **`isort`**: Ferramenta para organizar imports Python.

✨ Conceitos Abordados
---------------------

-   **Estrutura de Pacotes:** Organização de arquivos em subdiretórios (`utils/`) para formar um pacote Python, utilizando o arquivo `__init__.py` para definir sua estrutura.

-   **Modularização:** Separação de responsabilidades em arquivos menores e mais específicos (ex: `calculos.py`, `validadores.py`), tornando o código mais legível e fácil de manter.

-   **Sistema de Imports:** Prática de como importar funções e módulos de outros pacotes para uso em diferentes arquivos, como o `main.py` e o `test_pacotes.py`.

-   **Ponto de Entrada (`if __name__ == "__main__":`):** Uso do `if __name__ == "__main__":` para garantir que o código de demonstração seja executado apenas quando o arquivo é rodado diretamente.

-   **Testes Unitários em Módulos:** Criação de testes para funções em módulos, demonstrando como testar um pacote modular.

📁 Estrutura do Projeto
-----------------------

```
2.11.6_modulos_e_pacotes/
├── utils/
│   ├── __init__.py
│   ├── calculos.py
│   └── validadores.py
├── main.py
└── test_pacotes.py

```

⚙️ Como Executar
----------------

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado e o ambiente virtual ativado.

1.  **Navegue até este diretório:**

    ```
    cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.6_modulos_e_pacotes

    ```

2.  **Execute o arquivo principal para ver a demonstração:**

    ```
    python main.py

    ```

    *Isso exibirá a saída das funções de cálculo e validação no console.*

3.  **Execute os testes unitários para validar a implementação:**

    ```
    python -m unittest test_pacotes.py

    ```

    *Você verá o resumo dos testes, indicando se passaram (`OK`).*