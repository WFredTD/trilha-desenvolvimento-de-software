# 📚 Minha Trilha em Desenvolvimento de Software: Exercícios e Módulos

Bem-vindo ao meu repositório pessoal de exercícios e módulos da minha Trilha de Desenvolvimento de Software. Este espaço é dedicado a consolidar meu aprendizado, aplicar conceitos em desafios práticos e servir como um portfólio de código, demonstrando minha evolução e habilidades.

Aqui você encontrará implementações de exercícios modulares, seguindo os passos da minha trilha de estudo. Para os projetos integradores mais amplos e que resolvem problemas reais, consulte o repositório dedicado: [A ser criado].

## 🌟 Sobre Minha Trilha de Estudo (Notion)

Minha jornada de aprendizado é detalhadamente documentada em uma trilha de estudos personalizada no Notion. Nela, você pode acompanhar meu progresso, ver resumos de conceitos, comandos essenciais, e muito mais.

* **Acesse minha Trilha de Estudo Completa aqui:** https://ebony-sphere-7b6.notion.site/Trilha-para-Desenvolvimento-de-Software-20edac67d6178099af40c363dfb90e7a

Esta trilha foi projetada para me levar desde os fundamentos de programação e Python até tópicos avançados de desenvolvimento web, automação inteligente, dados e cloud, construindo uma base sólida para uma carreira robusta em tecnologia.

## 📁 Estrutura do Repositório

Aqui você encontrará a organização dos exercícios por módulo/fase da trilha:

* **[Fase 1: Fundamentos Essenciais](fase_1_fundamentos_essenciais/README.md)**
    * **[Módulo 1: Git e GitHub](fase_1_fundamentos_essenciais/modulo_1_git_e_github/README.md)**
    * **[Módulo 2: Python Essencial](fase_1_fundamentos_essenciais/modulo_2_python_essencial/README.md)**
        * [2.11.1: Decorador de Log e Testes Unitários](fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.1_decoradores_e_testes/README.md)
        * [2.11.2: Expressões Regulares e Manipulação de Strings](#2112-expressoes-regulares-e-manipulacao-de-strings)
        * [...]
    * [Módulo 3: SQL Essencial e Excel](fase_1_fundamentos_essenciais/modulo_3_sql_essencial_e_excel/README.md)
        * [...]

* **[Fase 2: Desenvolvimento Web com Django](fase_2_desenvolvimento_web_com_django/README.md)**
    * [...]

* **[Fase 3: Qualificação para o Mercado](fase_3_qualificacao_para_o_mercado/README.md)**
    * [...]

*(Outras fases (e tecnologias, caso necessário) serão adicionadas conforme o progresso da trilha.)*


## ⚙️ Como Utilizar Este Repositório

Este repositório utiliza o **`uv`** como gerenciador de pacotes e ambientes virtuais, uma ferramenta moderna e extremamente rápida para o ecossistema Python.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/WFredTD/trilha-desenvolvimento-de-software
    cd trilha-desenvolvimento-de-software
    ```
2.  **Instale o `uv` (Gerenciador de Pacotes):**
    * `uv` é um gerenciador de pacotes e criador de ambientes virtuais que substitui `pip` e `venv` tradicionalmente. Ele é construído em Rust para ser ultrarrápido.
    * Certifique-se de que o Python esteja instalado em seu sistema.
    * Para instalar o `uv` no Windows (via PowerShell):
        ```powershell
        irm https://astral.sh/uv/install.ps1 | iex
        ```
    * Para outras plataformas, consulte a documentação oficial do `uv` (ex: `pip install uv` pode funcionar em algumas configurações).
3.  **Crie e ative o ambiente virtual com `uv` (na raiz do repositório):**
    ```bash
    uv venv
    # No Windows (PowerShell):
    .\.venv\Scripts\Activate.ps1
    # No Windows (CMD/Git Bash):
    .\.venv\Scripts\activate
    # No macOS/Linux:
    source ./.venv/bin/activate
    ```
    * **Importante:** Verifique se o prompt do seu terminal mostra `(.venv)` ou similar, indicando que o ambiente está ativado.
4.  **Navegue até a pasta do exercício/módulo desejado.**
    * Exemplo: `cd modulo_2_python_essencial/2.11.1_decoradores_e_testes`
5.  **Instale as dependências específicas do exercício com `uv`:**
    * Cada `README.md` de exercício indicará as dependências (ex: `uv pip install black isort`). Se houver um `requirements.txt` na pasta, use `uv pip install -r requirements.txt`.
6.  **Siga as instruções no `README.md` específico de cada exercício.**
    * Cada pasta de exercício terá seu próprio `README.md` com instruções detalhadas de como rodar o código e quais conceitos foram abordados.

## 📝 Contato

Walter Friedrich Torres Dreyer
https://www.linkedin.com/in/walterftdreyer/

---

### Módulos e Fases Detalhadas

*(Esta seção terá links âncora para os títulos acima. Por enquanto, é apenas uma estrutura.)*

#### Fase 1: Fundamentos Essenciais

* **[Módulo 1: Git e GitHub para Colaboração](fase_1_fundamentos_essenciais/modulo_1_git_e_github/README.md)**
    * *Visão Geral:* Cobrirá os fundamentos de sistemas de controle de versão, rastreamento de mudanças e colaboração em projetos de código.

* **[Módulo 2: Python Essencial (Revisão Orientada a Objetos e Estruturas de Dados)](fase_1_fundamentos_essenciais/modulo_2_python_essencial/README.md)**
    * *Visão Geral:* Aprofundará os conceitos de Python, desde a sintaxe básica até tópicos avançados como POO, módulos, pacotes, expressões regulares e testes unitários.

    * **[2.11.1: Decorador de Log e Testes Unitários](fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.1_decoradores_e_testes/README.md)**
        * *Um exercício prático para aplicar o uso de decoradores, `*args`, `**kwargs`, `functools.wraps` e a escrita de testes unitários com `unittest`.*

    * **[2.11.2: Expressões Regulares e Manipulação de Strings](fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.2_expressoes_regulares_e_manipulacao_de_strings/README.md)**
        * *Próximo conjunto de exercícios para explorar a busca, validação e extração de padrões em texto usando o módulo `re`.*