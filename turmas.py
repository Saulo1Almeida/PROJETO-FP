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
   
   def criar_turma():
    
    conn = create_connection()
    if conn is None:
        return
    
    nome = input("Digite o nome da turma: ")
    professor_id_str = input("ID do professor responsável pela turma (deixe vazio se não houver): ")
    professor_id = int(professor_id_str) if professor_id_str.isdigit() else None
    
    if professor_id:
        check_prof_query = "SELECT id FROM professores WHERE id = ?"
        if not execute_read_query(conn, check_prof_query, (professor_id,)):
            print(f"Professor com ID {professor_id} não encontrado. Turma será criada sem professor responsável.")
            professor_id = None

    insert_query = "INSERT INTO turmas (nome, professor_id) VALUES (?, ?)"
    turma_id = execute_query(conn, insert_query, (nome, professor_id))

    conn.close()
    
    if turma_id:
        print(f"Turma '{nome}' (ID: {turma_id}) criada com sucesso!\n")
    else:
        print(f"Erro ao criar turma '{nome}'.")


