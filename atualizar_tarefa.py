def atualizar_tarefa(tarefas, index_tarefa):
    if index_tarefa < 1 or index_tarefa > len(tarefas):
        print("Número da tarefa inválido.")
        return
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas[index_tarefa - 1]["tarefa"] = nova_tarefa
    print(f"Tarefa {index_tarefa} atualizada para: {nova_tarefa}")