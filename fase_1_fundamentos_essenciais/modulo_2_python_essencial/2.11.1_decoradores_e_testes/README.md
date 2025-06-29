# 💡 Exercício 2.11.1: Decorador de Log e Testes Unitários em Python

Este diretório contém a solução para o Exercício 2.11.1 da minha Trilha de Desenvolvimento de Software. O objetivo deste exercício foi praticar os conceitos de Funções Avançadas, Decoradores e Testes Unitários, além de aplicar boas práticas de estilo de código.

## 🚀 Tecnologias e Módulos Utilizados

* **Python 3.x**
* **Módulo `functools`**: Utilizado para o decorador `@functools.wraps`.
* **Módulo `unittest`**: Framework de testes unitários built-in do Python.
* **`uv`**: Gerenciador de pacotes e ambientes virtuais.
* **`black`**: Formatador de código Python.
* **`isort`**: Ferramenta para organizar imports Python.

## ✨ Conceitos Abordados

Este exercício me permitiu aprofundar e aplicar os seguintes conceitos do Módulo 2 de Python Essencial:

* **Funções como Cidadãos de Primeira Classe:** A capacidade de passar funções como argumentos e retorná-las.
* **Decoradores:** Criação e aplicação de um decorador (`log_chamada`) para estender o comportamento de funções sem modificá-las diretamente.
* **`*args` e `**kwargs`:** Utilização de argumentos posicionais e nomeados variáveis em funções e decoradores, permitindo flexibilidade na assinatura de funções.
* **`functools.wraps`:** Preservação de metadados da função original (`__name__`, `__doc__`) após a decoração.
* **Tratamento de Exceções:** Implementação de `ValueError` para cenários de erro esperados (ex: divisão por zero).
* **Testes Unitários (`unittest`):**
    * Escrita de casos de teste (`unittest.TestCase`).
    * Uso de métodos de asserção (`assertEqual`, `assertAlmostEqual`, `assertRaises`) para verificar o comportamento esperado das funções.
    * Prática de documentação de testes.
* **Boas Práticas e Estilo de Código (PEP 8):**
    * Nomenclatura (CamelCase para classes, snake_case para funções/variáveis).
    * Docstrings (módulos, classes, funções e decoradores).
    * Organização de imports (com `isort`).
    * Formatação automática de código (com `black`).

## 📁 Estrutura do Projeto

```
2.11.1_decoradores_e_testes/
├── meu_modulo.py             # Contém o decorador 'log_chamada' e as funções decoradas.
├── test_meu_modulo.py        # Contém os testes unitários para as funções em meu_modulo.py.
└── README.md                 # Este arquivo.
```

## ⚙️ Como Executar

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado globalmente e o repositório clonado, conforme as instruções no [README.md principal](../../../README.md) do repositório.

1.  **Navegue até este diretório:**
    ```bash
    cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.1_decoradores_e_testes
    ```
2.  **Ative o ambiente virtual (`.venv`)** criado na raiz do repositório:
    * No Windows (PowerShell): `..\..\..\.venv\Scripts\Activate.ps1`
    * No Windows (CMD/Git Bash): `..\..\..\.venv\Scripts\activate`
    * No macOS/Linux: `source ../../../.venv/bin/activate`
    * (O prompt do seu terminal deve mudar para indicar que o ambiente está ativado, ex: `(.venv)`)
3.  **Instale as dependências específicas deste exercício:**
    ```bash
    uv pip install black isort
    ```
4.  **Execute o módulo principal para ver a demonstração das funções decoradas:**
    ```bash
    python meu_modulo.py
    ```
    *Você verá as mensagens de log geradas pelo decorador no console.*

5.  **Execute os testes unitários:**
    ```bash
    python -m unittest test_meu_modulo.py
    # Ou, se preferir rodar diretamente o arquivo de testes:
    # python test_meu_modulo.py
    ```
    *Você verá o resumo dos testes, indicando se passaram (`OK`) ou falharam (`FAILED`).*

---