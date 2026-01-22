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
        self.__livros_emprestados = []

    def adicionar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def remover_livro(self, livro):
        self.__livros_emprestados.remove(livro)

    def listar_livros(self):
        return self.__livros_emprestados

    def possui_livro(self, livro):
        return livro in self.livros_emprestados

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if self.livros:
            for i, l in enumerate(self.livros, start=1):
                print(f"{i} - Titulo: {l.titulo}, Autor: {l.autor}, Genero: {l.genero}, Dispovel: {'Sim' if l.esta_disponivel()  else 'Não'}")
        else:
            print("A biblioteca está vazia.")

    def listar_livros_emprestados(self, usuario):
        if usuario.listar_livros():
            print(f"\nLivros alugados do usuário '{usuario.nome}': ")
            for i, livro in enumerate(usuario.listar_livros(), start=1):
                print(f"{i} - Titulo: {livro.titulo}, Autor: {livro.autor}, Genero: {livro.genero}")
        else:
            print(f"O usuário '{usuario.nome}' não tem livros emprestados.")

    def emprestar_livro(self, livro, usuario):
        if livro.emprestar():
            usuario.adicionar_livro(livro)
            print(f"\nLivro '{livro.titulo}' foi  emprestado para {usuario.nome}")
            return True
        print("Livro indisponível para empréstimo.")
        return False

    def encontrar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def encontrar_usuario(self, nome, usuarios):
        for usuario in usuarios:
            if usuario.nome == nome:
                return usuario
        return None

    def devolver_livro(self, livro, usuario):
        if usuario.possui_livro(livro):
            usuario.devolver_livro(livro)
            livro.devolver()
            print(f"\nLivro '{livro.titulo}' foi devolvido pelo {usuario.nome}")
            return True
        print("Esse livro nao esta com o usuario.")
        return False

def main():
    biblioteca = Biblioteca()
    usuarios = []
    #livros = []
    print("\nBem vindo ao sistema de biblioteca!")
    while True:
        print("""\nMenu de Opções: 
        1. Adicionar livro
        2. Listar livros
        3. Cadastrar usuário
        4. Alugar livro
        5. Listar livros alugados
        6. Devolver livro
        7. Sair
        """)

        opcao = input("Digite a opção desejada: ")

        match opcao:
            case "1":
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                genero = input("Digite o gênero do livro: ")
                livro = Livro(titulo, autor, genero)
                biblioteca.adicionar_livro(livro)
                print(f"O livro '{titulo}' foi adicionado com sucesso.")

            case "2":
                print("\nCatalogo da Biblioteca: ")
                biblioteca.listar_livros()

            case "3":
                nome = input("Digite o nome do usuário: ")
                usuarios.append(Usuario(nome)) 
                print(f"O usuário '{nome}' foi cadastrado com sucesso.")

            case "4":
                titulo = input("Digite o título do livro a ser alugado: ")
                usuario_aluga = input("Digite o nome do usuário que vai alugar o livro: ")
                livro_encontrado = biblioteca.encontrar_livro(titulo)
                usuario_encontrado = biblioteca.encontrar_usuario(usuario_aluga, usuarios) 
                if livro_encontrado and usuario_encontrado:
                    biblioteca.emprestar_livro(livro_encontrado, usuario_encontrado)
                else:
                    print("Livro ou Usuario não encontrado.")

            case "5":
                nome = input("Digite o nome do usuario que deseja mostrar os livros alugados: ")
                usuario_encontrado = biblioteca.encontrar_usuario(nome, usuarios)
                if usuario_encontrado:
                    biblioteca.listar_livros_emprestados(usuario_encontrado)
                else:
                    print("Livro não encontrado.")

            case "6":
                titulo = input("Digite o título do livro que foi devolvido: ")
                usuario = input("Digite o nome do usuário devolveu o livro: ")
                livro_encontrado = biblioteca.encontrar_livro(titulo)
                usuario_encontrado = biblioteca.encontrar_usuario(usuario, usuarios)
                if livro_encontrado:
                    biblioteca.devolver_livro(livro_encontrado, usuario_encontrado)
                else:
                    print("Livro não encontrado.")

            case "7":
                print("Saindo do programa...")
                break

            case _:
                print("Opcao invalida!")

main()

"""
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
livro2 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", "Fantasia")
livro3 = Livro("Percy Jackson e o Ladrao de Raios", "Rick Riordan", "Ficção")

"""