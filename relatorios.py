from database import create_connection, execute_read_query

def relatorio_alunos_por_turma():
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
