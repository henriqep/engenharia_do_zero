biblioteca = {
    'disponiveis': [],
    'alugados': []
}

def listar_livros(categoria, titulo_categoria):
    print(f"\n{titulo_categoria}: ")
    livros = biblioteca[categoria]

    if not livros:
        print("Nenhum livro para listar.")
        return

    for i, (titulo, autor) in enumerate(livros, start=1):
        print(f"{i} - Titulo: {titulo} | Autor: {autor}")

def adicionar_livro(titulo, autor):
    biblioteca['disponiveis'].append((titulo, autor))
    print(f"O livro '{titulo}' de {autor} foi adicionado com sucesso.")

def mover_livro(titulo, origem, destino, acao):
    for i, (t, a) in enumerate(biblioteca[origem]):
        if t == titulo:
            livro = biblioteca[origem].pop(i)
            biblioteca[destino].append(livro)
            print(f"O livro '{titulo}' foi {acao} com sucesso!")
            return
    print(f"O livro '{titulo}' nao esta disponivel ou nao existe.")

def remover_livro(titulo):
    for i, (t, _) in enumerate(biblioteca['disponiveis']):
        if t == titulo:
            biblioteca['disponiveis'].pop(i)
            print(f"O livro '{titulo}' foi removido com sucesso.")
            return
    print(f"O livro '{titulo}' nao esta disponivel para remover ou nao existe.")

while True:
    print("""
Menu de Opções:
1. Listar livros disponíveis
2. Adicionar livro
3. Remover livro
4. Alugar livro
5. Listar livros alugados
6. Devolver livro
7. Sair
""")

    opcao = input("Escolha uma opcao: ")

    match opcao:
        case "1":
            listar_livros("disponiveis", "Livros Disponiveis")

        case "2":
            titulo = input("Digite o titulo: ")
            autor = input("Digite o autor: ")
            adicionar_livro(titulo, autor)

        case "3":
            titulo = input("Digite o titulo do livro a ser removido: ")
            remover_livro(titulo)

        case "4":
            titulo = input("Digite o titulo do livro a ser alugado: ")
            mover_livro(titulo, "disponiveis", "alugados", "alugado")
        
        case "5":
            listar_livros("alugados", "Livros Alugados")

        case "6":
            titulo = input("Digite o titulo do livro a ser devolvido: ")
            mover_livro(titulo, "alugados", "disponiveis", "devolvido")

        case "7":
            print("Saindo do programa! ")
            break

        case _:
            print("Opcao invalida! ")