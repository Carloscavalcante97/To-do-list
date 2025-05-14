from adicionar_tarefa import adicionar_tarefa
from listar_tarefas import listar_tarefas
from atualizar_tarefa import atualizar_tarefa
from completar_tarefa import completar_tarefa
from deletar_tarefa import deletar_tarefa

tarefas = []

while True:
    print("\nMenu de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    try:
        entrada =input("Escolha uma opção: ").strip()
        opcao_menu = int(entrada)
        
        if opcao_menu == 1:
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefas, nova_tarefa)
        elif opcao_menu == 2:
            listar_tarefas(tarefas)
        elif opcao_menu == 3:
            listar_tarefas(tarefas)
            index_tarefa = int(input("Digite o número da tarefa a ser atualizada: "))
            atualizar_tarefa(tarefas, index_tarefa)
        elif opcao_menu == 4:
            listar_tarefas(tarefas)
            index_tarefa = int(input("Digite o número da tarefa a ser completada: "))
            completar_tarefa(index_tarefa, tarefas)
        elif opcao_menu == 5:
            deletar_tarefa( tarefas)
        elif opcao_menu == 6:
            print("Saindo do programa...")
            break
    except ValueError:
       print("Por favor, digite um número válido.")

        
       
    