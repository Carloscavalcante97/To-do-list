def completar_tarefa(tarefa_index, tarefas):
    if tarefa_index < 1 or tarefa_index > len(tarefas):
        print("Número da tarefa inválido.")
        return
    tarefas[tarefa_index - 1]["completada"] = True
    return print(f"Tarefa {tarefa_index} marcada como completada.")
