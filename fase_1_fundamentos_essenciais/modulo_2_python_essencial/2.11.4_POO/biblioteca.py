from abc import ABC, abstractmethod


class Material(ABC):
    """
    Classe base abstrata que representa um material genérico de uma biblioteca.

    Define a interface comum (o método 'exibir_informacoes') e os atributos
    básicos que todas as suas subclasses devem possuir.

    Args:
        titulo (str): O título do material (nome do livro ou revista).
        autor (str): O autor ou criador do material.
    """

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    @abstractmethod
    def exibir_informacoes(self):
        """
        Método abstrato que deve ser implementado nas subclasses.
        Retorna uma string formatada com as informações do material.
        """
        pass

    def get_titulo(self):
        """
        Retorna o título do material.

        Returns:
            str: O título do material.
        """
        return self.__titulo

    def get_autor(self):
        """
        Retorna o autor do material.

        Returns:
            str: O autor do material.
        """
        return self.__autor


class Livro(Material):
    """
    Representa um livro na biblioteca.

    Args:
        titulo (str): O título do livro.
        autor (str): O autor do livro.
        isbn (str): O número de identificação único do livro.
    """

    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor)
        self.__isbn = isbn

    def exibir_informacoes(self):
        """
        Retorna uma string com as informações do livro.

        Returns:
            str: Uma string formatada com o título, autor e ISBN.
        """
        return f"Livro: {self.get_titulo()}, Autor: {self.get_autor()}, ISBN: {self.__isbn}"

    def get_isbn(self):
        """
        Retorna o ISBN do livro.

        Returns:
            str: O ISBN do livro.
        """
        return self.__isbn


class Revista(Material):
    """
    Representa uma revista na biblioteca.

    Args:
        titulo (str): O título da revista.
        autor (str): O autor da revista.
        edicao (str): A edição da revista.
    """

    def __init__(self, titulo, autor, edicao):
        super().__init__(titulo, autor)
        self.__edicao = edicao

    def exibir_informacoes(self):
        """
        Retorna uma string com as informações da revista.

        Returns:
            str: Uma string formatada com o título, autor e edição.
        """
        return f"Revista: {self.get_titulo()}, Autor: {self.get_autor()}, Edição: {self.__edicao}"

    def get_edicao(self):
        """
        Retorna a edição da revista.

        Returns:
            str: A edição da revista.
        """
        return self.__edicao


class Biblioteca:
    """
    Representa um sistema de gerenciamento de biblioteca.

    Permite adicionar diferentes tipos de materiais (livros, revistas) e listá-los.
    """

    def __init__(self):
        """
        Construtor da classe Biblioteca. Inicializa uma lista vazia para os materiais.
        """
        self.__materiais = []

    def get_materiais(self):
        """
        Retorna a lista de materiais na biblioteca.

        Returns:
            list: Uma lista dos objetos de materiais na biblioteca.
        """
        return self.__materiais

    def adicionar_material(self, material):
        """
        Adiciona um material à biblioteca.

        Args:
            material (Material): O objeto Material a ser adicionado.
        """
        self.__materiais.append(material)
        print(f"{material.get_titulo()} adicionado à biblioteca.")

    def listar_materiais(self):
        """
        Lista todos os materiais na biblioteca, exibindo suas informações.

        O método demonstra o polimorfismo ao chamar a implementação correta de
        exibir_informacoes para cada tipo de material.
        """
        if not self.__materiais:
            print("A biblioteca está vazia.")
            return
        for material in self.__materiais:
            print(material.exibir_informacoes())


if __name__ == "__main__":
    biblioteca = Biblioteca()

    livro1 = Livro("Dom Casmurro", "Machado de Assis", "978-85-12345-67-8")
    revista1 = Revista("National Geographic", "Vários", "Maio 2023")
    livro2 = Livro("1984", "George Orwell", "978-0-451-52493-5")

    biblioteca.adicionar_material(livro1)
    biblioteca.adicionar_material(revista1)
    biblioteca.adicionar_material(livro2)

    print("\n--- Materiais na Biblioteca ---")
    biblioteca.listar_materiais()
