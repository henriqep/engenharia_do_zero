tarefas = []

def listar_tarefas():
    if len(tarefas) == 0:
        print("\nNão há tarefas na lista.")
    else:
        print("\nLista das TAREFAS: ")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa['titulo']} - status: {tarefa['concluida']}")

def adicionar_tarefa(tarefa):
    dict_tarefa = {'titulo': tarefa, 'concluida': " "}
    tarefas.append(dict_tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefas(posicao):
    if posicao >= 0 and posicao < len(tarefas):
        dict_tarefa = tarefas.pop(posicao)
        print(f"Tarefa '{dict_tarefa['titulo']}' removida com sucesso!")
    else:
        print("Posição inválida!")

def concluir_tarefa(posicao):
    if posicao >= 0 and posicao < len(tarefas):
        dict_tarefa = tarefas[posicao]
        dict_tarefa['concluida'] = "✔"
        print(f"Tarefa '{dict_tarefa['titulo']}' marcada como concluída.")
    else:
        print("Posicao invalida!")

while True:
    print("\nSeja bem-vindo ao Gerenciador de Tarefas!")
    print("1. Listar Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Remover Tarefa")
    print("4. Concluir Tarefa")
    print("5. Sair")

    opcao = input("\nDigite a opção desejada: ")
    
    if opcao == '1':
        listar_tarefas()
    if opcao == '2':
        tarefa = input("Digite uma nova tarefa: ")
        adicionar_tarefa(tarefa)
    if opcao == '3':
        listar_tarefas()
        posicao = int(input("Digite a posição da tarefa que deseja remover: "))
        remover_tarefas(posicao-1)
    if opcao == '4':
        listar_tarefas()
        posicao = int(input("Digite a posição da tarefa que deseja concluir: "))
        print(posicao)
        concluir_tarefa(posicao-1)
    if opcao == '5':
        print("Saindo do programa...")
        break
