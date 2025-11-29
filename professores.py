from database import create_connection, execute_query, execute_read_query

def buscar_professor_por_id(conn, id_professor):
    """Busca um professor pelo ID no banco de dados."""
    query = "SELECT * FROM professores WHERE id = ?"
    result = execute_read_query(conn, query, (id_professor,))
    return result[0] if result else None

def listar_professores():
    """Lista todos os professores cadastrados."""
    conn = create_connection()
    if conn is None:
        return

    professores = execute_read_query(conn, "SELECT * FROM professores")
    conn.close()
if not professores:
    print("\n Nenhum professor cadastrado.\n")
    return
print("\n Lista de Professores: \n")
for p in professores:
    print(f"ID: {p['id']} | Matrícula: {p['matricula']} | Nome: {p['nome']} | Disciplina: {p['disciplina']}")
print()

