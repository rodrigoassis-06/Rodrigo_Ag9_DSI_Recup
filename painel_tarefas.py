# ==============================================================================
# Atividade: Desafio Visual - Meu Painel de Dados com Listas
# Agenda 09 - Desenvolvimento de Sistemas I (Recuperacao)
# Aluno: Rodrigo Assis
# ==============================================================================

def executar_painel(nome, cidade, tarefas):
    """
    Processa a lista de tarefas e determina a mensagem de rotina
    com base na quantidade de tarefas (len).
    """
    total = len(tarefas)
    if total == 0:
        mensagem = "Nenhuma tarefa cadastrada."
    elif total <= 2:
        mensagem = f"{nome} de {cidade}: rotina leve hoje!"
    else:
        mensagem = f"{nome} de {cidade}: rotina cheia! Organize prioridades."
    return mensagem


def main():
    print("=" * 50)
    print("      MEU PAINEL DE DADOS - ROTINA DIARIA       ")
    print("=" * 50)

    nome = input("Digite seu nome: ").strip()
    cidade = input("Digite sua cidade: ").strip()

    tarefas = []
    try:
        qtd = int(input("Quantas tarefas você vai cadastrar? "))
    except ValueError:
        qtd = 0

    for i in range(qtd):
        tarefa = input(f"Digite a tarefa {i+1}: ").strip()
        tarefas.append(tarefa)

    print("\nTarefas cadastradas:")
    for t in tarefas:
        print("-", t)

    mensagem_final = executar_painel(nome, cidade, tarefas)
    print("\n" + mensagem_final)
    print("=" * 50)


if __name__ == "__main__":
    main()
