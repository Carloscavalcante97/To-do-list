def adicionar_tarefa (tarefas ,nova_tarefa):
    tarefa = {"tarefa": nova_tarefa, "completada": False}
    if (nova_tarefa == ""):
        print("Tarefa não pode ser vazia.")
        return
    tarefas.append(tarefa)
    print(f"Tarefa {nova_tarefa} adicionada com sucesso!")
    return