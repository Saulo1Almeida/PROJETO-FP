from database import create_connection, execute_query, execute_read_query 


def buscar_professor_por_id(conn, id_professor):
    query = "SELECT * FROM professores WHERE id = ?"
    result = execute_read_query(conn, query, (id_professor,))
    return result[0] if result else None


def listar_professores():
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
    listar_professores()


def ler_um_professor():
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


def atualizar_professor():
    conn = create_connection()
    if conn is None:
        return

    listar_professores()

    id_digitado = input("\n Digite o ID do professor que deseja atualizar: ")
    if not id_digitado.isdigit():
        print("\n ID inválido. Digite apenas números.\n")
        conn.close()
        return
    id_professor = int(id_digitado)
    
    professor = buscar_professor_por_id(conn, id_professor)

    if not professor:
        print("\n Professor não encontrado.\n")
        conn.close()
        return

    print(f"Editando: {professor['nome']}")
    
    novo_nome = input(f"Novo nome (Atual: {professor['nome']}): ") or professor["nome"]
    nova_matricula = input(f"Nova matrícula (Atual: {professor['matricula']}): ") or professor["matricula"]
    nova_disciplina = input(f"Nova disciplina (Atual: {professor['disciplina']}): ") or professor["disciplina"]
    
    update_query = "UPDATE professores SET nome = ?, matricula = ?, disciplina = ? WHERE id = ?"
    execute_query(conn, update_query, (novo_nome, nova_matricula, nova_disciplina, id_professor))
    
    conn.close()
    print("\n Professor atualizado com sucesso!\n")


def deletar_professor():
    conn = create_connection()
    if conn is None:
        return

    listar_professores()
    id_digitado = input("Digite o ID do professor que deseja excluir: ")
    if not id_digitado.isdigit():
        print("\n ID inválido. Digite apenas números.\n")
        conn.close()
        return
    id_professor = int(id_digitado)
    
    professor = buscar_professor_por_id(conn, id_professor)

    if not professor:
        print("Professor não encontrado.\n")
        conn.close()
        return
    
    check_turmas_query = "SELECT id FROM turmas WHERE professor_id = ?"
    if execute_read_query(conn, check_turmas_query, (id_professor,)):
        print("\n Erro: O professor está associado a uma ou mais turmas. Remova a associação antes de excluir.\n")
        conn.close()
        return

    delete_query = "DELETE FROM professores WHERE id = ?"
    execute_query(conn, delete_query, (id_professor,))
    
    conn.close()
    print(f"Professor '{professor['nome']}' removido com sucesso!\n")
    
