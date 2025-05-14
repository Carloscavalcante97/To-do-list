def deletar_tarefa( tarefas):
    tarefas[:] =[tarefa for tarefa in tarefas if not tarefa["completada"] ]
    print("Tarefas deletada com sucesso.")