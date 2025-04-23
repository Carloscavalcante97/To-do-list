def deletar_tarefa(index_tarefa, tarefas):
    if index_tarefa < 1 or index_tarefa > len(tarefas):
        print("Número da tarefa inválida.")
        return
    tarefas.pop(index_tarefa - 1)
    return print(f"Tarefa {index_tarefa} deletada com sucesso.")