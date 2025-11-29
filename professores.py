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
