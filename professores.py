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
def criar_professor():
    """Cria um novo professor no banco de dados."""
    conn = create_connection()
    if conn is None:
        return

    nome = input("\n Nome do Professor: \n ")
    matricula = input(" \n Matrícula: \n ")
    disciplina = input(" \n Disciplina ministrada: \n")

    check_query = "SELECT id FROM professores WHERE matricula = ?"
    if execute_read_query(conn, check_query, (matricula,)):
        print("\n Matrícula já cadastrada.\n")
        conn.close()
        return

    insert_query = "INSERT INTO professores (nome, matricula, disciplina) VALUES (?, ?, ?)"
    professor_id = execute_query(conn, insert_query, (nome, matricula, disciplina))
    
    conn.close()
if professor_id:
    print(f"Professor '{nome}' (ID: {professor_id}) adicionado com sucesso!\n")
else:
    print(f"Erro ao adicionar professor '{nome}'.")

def ler_professores():
    """Exibe a lista de todos os professores."""
    listar_professores()

def ler_um_professor():
    """Exibe os detalhes de um professor específico."""
    conn = create_connection()
    if conn is None:
        return
    id_digitado = input("Digite o ID do professor: ")

if not id_digitado.isdigit():
    print("\n ID inválido. Digite apenas números.\n")
    conn.close()
    return
id_professor = int(id_digitado)

professor = buscar_professor_por_id(conn, id_professor)
if professor:
    print("\nDetalhes do Professor:")
    print(f"ID: {professor['id']}")
    print(f"Nome: {professor['nome']}")
    print(f"Matrícula: {professor['matricula']}")
    print(f"Disciplina: {professor['disciplina']}\n")
else:
    print("\n Professor não encontrado.\n")
    
conn.close()
