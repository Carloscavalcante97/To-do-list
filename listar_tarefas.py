def listar_tarefas(tarefas):
    if len(tarefas) < 1:
        print("Nenhuma tarefa encontrada.")
        return
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[✔️ ]" if tarefa["completada"] else "[ ]"
        print(f"{i}. {tarefa['tarefa']} {status}")
