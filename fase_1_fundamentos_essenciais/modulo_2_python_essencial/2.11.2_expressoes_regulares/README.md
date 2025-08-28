💡 Exercício 2.11.2: Expressões Regulares e Manipulação de Strings
==================================================================

Este diretório contém a solução para o Exercício 2.11.2 da minha Trilha de Desenvolvimento de Software. O objetivo deste exercício foi praticar a aplicação de expressões regulares (`RegEx`) para validação e extração de dados, além de reforçar o conceito de Programação Orientada a Objetos (POO) e testes unitários.

🚀 Tecnologias e Módulos Utilizados
-----------------------------------

*   **Python 3.x**
    
*   **Módulo `re`**: Módulo built-in do Python para operações com expressões regulares.
    
*   **Módulo `unittest`**: Framework de testes unitários.
    
*   **`uv`**: Gerenciador de pacotes e ambientes virtuais.
    
*   **`black`**: Formatador de código Python.
    
*   **`isort`**: Ferramenta para organizar imports Python.
    

✨ Conceitos Abordados
---------------------

Este exercício me permitiu aprofundar e aplicar os seguintes conceitos do Módulo 2 de Python Essencial:

*   **Expressões Regulares (RegEx):** Criação de padrões para:
    
    *   Validar o formato de strings (ex: endereços de e-mail).
        
    *   Extrair dados específicos de um texto (ex: URLs).
        
    *   Substituir ou formatar partes de uma string (ex: remover espaços múltiplos ou caracteres especiais).
        
*   **Programação Orientada a Objetos (POO):** Encapsulamento de funcionalidades de processamento de texto em uma classe (`ProcessadorDeDados`).
    
*   **Testes Unitários (unittest):**
    
    *   Escrita de casos de teste para métodos de classe.
        
    *   Uso de `self.assertTrue`, `self.assertFalse` e `self.assertEqual` para verificar resultados.
        
    *   Prática de documentação de testes.
        
*   **Boas Práticas e Estilo de Código (PEP 8):**
    
    *   Uso de docstrings para classes e métodos.
        
    *   Formatação automática de código com `black` e `isort`.
        
*   **Raciocínio Lógico e Depuração:** Análise de `tracebacks` e depuração de padrões RegEx, um processo crucial para o desenvolvimento de software robusto.
    

📁 Estrutura do Projeto
-----------------------

```
2.11.2_expressoes_regulares/
├── processador_strings.py
├── test_processador.py
└── README.md
```

⚙️ Como Executar
----------------

Para rodar este exercício, siga os passos abaixo. Certifique-se de que o `uv` já esteja instalado e o ambiente virtual ativado, conforme as instruções no [README.md principal](../../../README.md).

Navegue até este diretório:

```
cd fase_1_fundamentos_essenciais/modulo_2_python_essencial/2.11.2_expressoes_regulares
```

Execute o módulo principal para ver a demonstração das funções:

```
python processador_strings.py
```
Você verá as saídas de validação e extração no console.

Execute os testes unitários:

```
python -m unittest test_processador.py
```
Você verá o resumo dos testes, indicando se passaram (`OK`) ou falharam (`FAILED`).