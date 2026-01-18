livros_disponiveis = []
livros_alugados = []

def listar_livros(opcao):
    if opcao == 1:
        print("Livros Disponiveis: ")
        if livros_disponiveis:
            cont = 1
            for l, a in livros_disponiveis:
                print(f'{cont} - Titulo: {l} - Autor: {a}')
                cont += 1
        else:
            print("Não há livros disponíveis para listar.")
    if opcao == 5:
        print("Livros Alugados: ")
        if livros_alugados:
            cont = 1
            for l, a in livros_alugados:
                print(f'{cont} - Titulo: {l} - Autor: {a}')
                cont += 1
        else:
            print("Não há livros alugados para listar.")

def adicionar_livro(titulo, autor):
    livros_disponiveis.append((titulo, autor))
    print(f"O livro '{titulo}' de {autor} foi adicionado com sucesso.")

def remover_livro(titulo):
    if any(tupla[0] == titulo for tupla in livros_disponiveis):
        for i, tupla in enumerate(livros_disponiveis):
            if tupla[0] == titulo:
                del livros_disponiveis[i]
                print(f"O livro '{titulo}' foi removido com sucesso.")
                break
    else:
        print(f"O livro '{titulo}' não está disponível para remover.")

def alugar_livro(titulo):
    if any(tupla[0] == titulo for tupla in livros_disponiveis):
        for i, tupla in enumerate(livros_disponiveis):
            if tupla[0] == titulo:
                livro = livros_disponiveis.pop(i)
                livros_alugados.append(livro)
                print(f"O livro '{titulo}' foi alugado com sucesso.")
                break
    else:
        print(f"O livro '{titulo}' não está disponível para alugar.")

def devolver_livro(titulo):
    if any(tupla[0] == titulo for tupla in livros_alugados):
        for i, tupla in enumerate(livros_alugados):
            if tupla[0] == titulo:
                livro = livros_alugados.pop(i)
                livros_disponiveis.append(livro)
                print(f"O livro '{titulo}' foi devolvido com sucesso.")
                break
    else:
        print(f"O livro '{titulo}' não está disponível para devolver.")


while True:
    print("\nMenu de Opções:")
    print("1. Listar livros disponíveis.")
    print("2. Adicionar livro.")
    print("3. Remover Livro.")
    print("4. Alugar Livro.")
    print("5. Listar livros alugados.")
    print("6. Devolver Livro.")
    print("7. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1 or opcao == 5:
        listar_livros(opcao)

    if opcao == 2:
        titulo = input("Digite o titulo do livro que deseja adicionar: ")
        autor = input("Digite o autor do livro que deseja adicionar: ")
        adicionar_livro(titulo, autor)

    if opcao == 3:
        titulo = input("Digite o titulo do livro que deseja remover: ")
        remover_livro(titulo)

    if opcao == 4:
        titulo = input("Digite o titulo do livro que deseja alugar: ")
        alugar_livro(titulo)

    if opcao == 6:
        titulo = input("Digite o titulo do livro que deseja devolver: ")
        devolver_livro(titulo)

    if opcao == 7:
        print("Saindo do programa...")
        break
