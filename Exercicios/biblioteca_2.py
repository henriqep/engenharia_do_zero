class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def possui_livro(self, livro):
        return livro in self.livros_emprestados

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for i, l in enumerate(self.livros, start=1):
            print(f"{i} - Titulo: {l.titulo}, Autor: {l.autor}, Genero: {l.genero}, Dispovel: {'Sim' if l.esta_disponivel()  else 'Não'}")
        return

    def emprestar_livro(self, livro, usuario):
        if livro.emprestar():
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
            print(f"Livro '{livro.titulo}' foi  emprestado para {usuario.nome}")
            return True
        print("Livro indisponível para empréstimo.")
        return False

    def devolver_livro(self, livro, usuario):
        if usuario.possui_livro(livro):
            usuario.livros_emprestados.remove(livro)
            livro.devolver()
            print(f"Livro '{livro.titulo}' foi devolvido pelo {usuario.nome}")
            return True
        print("Esse livro nao esta com o usuario.")
        return False

biblioteca = Biblioteca()
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", "Fantasia")
livro3 = Livro("Percy Jackson e o Ladrao de Raios", "Rick Riordan", "Ficção")

user1 = Usuario("Alice")
user2 = Usuario("Bob")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.emprestar_livro(livro1, user1)
biblioteca.emprestar_livro(livro2, user1)
biblioteca.emprestar_livro(livro2, user2)
print(user1.livros_emprestados)
print(user2.livros_emprestados)
biblioteca.listar_livros()
