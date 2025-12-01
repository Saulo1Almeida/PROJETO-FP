from database import create_connection, execute_query, execute_read_query

def buscar_turma_por_id(conn, id_turma):
   
    query = "SELECT * FROM turmas WHERE id = ?"
    result = execute_read_query(conn, query, (id_turma,))
    return result[0] if result else None

def listar_turmas():
   
    conn = create_connection()
    if conn is None:
        return

    query = """
    SELECT 
        t.id, 
        t.nome, 
        t.professor_id, 
        p.nome AS nome_professor
    FROM 
        turmas t
    LEFT JOIN 
        professores p ON t.professor_id = p.id
    """
    turmas = execute_read_query(conn, query)
    conn.close()
    if not turmas:
        print("Nenhuma turma cadastrada.\n")
        return

    print("\nLista de Turmas:")
    for t in turmas:
        professor_info = f"Professor: {t['nome_professor']} (ID: {t['professor_id']})" if t['professor_id'] else "N/A"
        print(f"ID: {t['id']} | Nome: {t['nome']} | {professor_info}")
    print()

