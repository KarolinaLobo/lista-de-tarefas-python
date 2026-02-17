ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def mostrar_menu():
    print("\n=== Lista de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

tarefas = carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova = input("Digite a nova tarefa: ")
        tarefas.append(nova)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        numero = int(input("Número da tarefa para remover: "))
        if 0 < numero <= len(tarefas):
            tarefas.pop(numero - 1)
            salvar_tarefas(tarefas)
            print("Tarefa removida!")
        else:
            print("Número inválido.")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
