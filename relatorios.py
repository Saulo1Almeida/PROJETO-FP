from database import create_connection, execute_read_query

def relatorio_alunos_por_turma():
    """Gera um relatório de alunos agrupados por turma."""
    conn = create_connection()
    if conn is None:
        return

    query = """
    SELECT 
        t.nome AS nome_turma, 
        a.nome AS nome_aluno, 
        a.matricula
    FROM 
        alunos a
    LEFT JOIN 
        turmas t ON a.turma_id = t.id
    ORDER BY 
        nome_turma, nome_aluno
    """
    dados = execute_read_query(conn, query)
    conn.close()

    if not dados:
        print("\n Não há dados de alunos ou turmas para gerar o relatório.\n")
        return

    print("\n========== RELATÓRIO DE ALUNOS POR TURMA ==========")
    turma_atual = None
    for row in dados:
        nome_turma = row['nome_turma'] if row['nome_turma'] else "SEM TURMA"
        if nome_turma != turma_atual:
            print(f"\n--- Turma: {nome_turma} ---")
            turma_atual = nome_turma
        print(f"  - Nome: {row['nome_aluno']} | Matrícula: {row['matricula']}")
    print("===================================================\n")

def relatorio_professores_por_disciplina():
    """Gera um relatório de professores agrupados por disciplina."""
    conn = create_connection()
    if conn is None:
        return

    query = """
    SELECT 
        disciplina, 
        nome, 
        matricula
    FROM 
        professores
    ORDER BY 
        disciplina, nome
    """
    dados = execute_read_query(conn, query)
    conn.close()

    if not dados:
        print("\n Não há dados de professores para gerar o relatório.\n")
        return

    print("\n========== RELATÓRIO DE PROFESSORES POR DISCIPLINA ==========")
    disciplina_atual = None
    for row in dados:
        if row['disciplina'] != disciplina_atual:
            print(f"\n--- Disciplina: {row['disciplina']} ---")
            disciplina_atual = row['disciplina']
        print(f"  - Nome: {row['nome']} | Matrícula: {row['matricula']}")
    print("=============================================================\n")

def relatorio_notas_alunos():
    """Gera um relatório de notas de todos os alunos."""
    conn = create_connection()
    if conn is None:
        return

    query = """
    SELECT 
        a.nome AS nome_aluno, 
        n.disciplina, 
        n.valor
    FROM 
        alunos a
    JOIN 
        notas n ON a.id = n.aluno_id
    ORDER BY 
        nome_aluno, disciplina
    """
    dados = execute_read_query(conn, query)
    conn.close()

    if not dados:
        print("\n Não há notas cadastradas para gerar o relatório.\n")
        return

    print("\n========== RELATÓRIO DE NOTAS DOS ALUNOS ==========")
    aluno_atual = None
    for row in dados:
        if row['nome_aluno'] != aluno_atual:
            print(f"\n--- Aluno: {row['nome_aluno']} ---")
            aluno_atual = row['nome_aluno']
        print(f"  - Disciplina: {row['disciplina']} | Nota: {row['valor']:.2f}")
    print("===================================================\n")

def exibir_menu_relatorios():
    """Exibe o menu de relatórios."""
    while True:
        print("\n========== MENU DE RELATÓRIOS ==========")
        print("1. Alunos por Turma")
        print("2. Professores por Disciplina")
        print("3. Notas dos Alunos")
        print("4. Voltar ao Menu Principal")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_alunos_por_turma()
        elif opcao == "2":
            relatorio_professores_por_disciplina()
        elif opcao == "3":
            relatorio_notas_alunos()
        elif opcao == "4":
            break
        else:
            print(" Opção inválida, Tente novamente.\n")
    
