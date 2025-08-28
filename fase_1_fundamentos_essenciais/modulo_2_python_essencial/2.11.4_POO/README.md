💡 Exercício 2.11.4: Programação Orientada a Objetos (POO)
==========================================================

Este diretório contém a solução para o Exercício 2.11.4 da minha Trilha de Desenvolvimento de Software. O objetivo foi aplicar os quatro pilares da Programação Orientada a Objetos (POO): **Abstração**, **Encapsulamento**, **Herança** e **Polimorfismo**, construindo um sistema de gerenciamento de biblioteca simples.

🚀 Tecnologias e Módulos Utilizados
-----------------------------------

-   **Python 3.x**

-   **Módulo `abc`**: Utilizado para definir classes e métodos abstratos, garantindo a implementação correta nas classes filhas.

-   **Módulo `unittest` e `unittest.mock`**: Usados para a criação de testes unitários, incluindo a técnica de `mock` para testar saídas de console.

-   **`uv`**: Gerenciador de pacotes e ambientes virtuais.

-   **`black`**: Formatador de código Python.

-   **`isort`**: Ferramenta para organizar imports Python.

✨ Conceitos Abordados
---------------------

-   **Abstração:** Criação de uma classe base (`Material`) que define uma interface comum (`exibir_informacoes()`) para suas subclasses (`Livro`, `Revista`), ocultando a complexidade da implementação.

-   **Herança:** Utilização do `super().__init__()` para permitir que classes filhas herdem atributos e comportamentos da classe pai (`Material`).

-   **Encapsulamento:** Proteção de atributos com o uso de dois underscores (`__`) e a criação de `getters` públicos para acesso controlado.

-   **Polimorfismo:** Implementação do método `listar_materiais()` na classe `Biblioteca`, que itera sobre diferentes tipos de objetos (`Livro`, `Revista`) e chama o mesmo método (`exibir_informacoes()`), mas obtendo um comportamento diferente para cada um.

-   **Testes de Unidade:** Validação do comportamento das classes, incluindo a criação de objetos, o acesso a getters e o teste de polimorfismo usando `unittest.mock` para verificar saídas de console.

📁 Estrutura do Projeto
-----------------------

```
2.11.4_POO/
├── biblioteca.py
├── test_biblioteca.py
└── README.md

```

⚙️ Como Executar
----------------

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado e o ambiente virtual ativado.

1.  **Navegue até este diretório:**

    ```
    cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.4_POO

    ```

2.  **Execute o módulo principal para ver a demonstração da POO em ação:**

    ```
    python biblioteca.py

    ```

    *Isso exibirá a lista formatada dos materiais na biblioteca.*

3.  **Execute os testes unitários para validar a implementação:**

    ```
    python -m unittest test_biblioteca.py

    ```

    *Você verá o resumo dos testes, indicando se passaram (`OK`).*