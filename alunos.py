from database import create_connection, execute_query, execute_read_query

def buscar_aluno_por_id(conn, id_aluno):
    """Busca um aluno pelo ID no banco de dados."""
    query = "SELECT * FROM alunos WHERE id = ?"
    result = execute_read_query(conn, query, (id_aluno,))
    return result[0] if result else None

def listar_alunos():
    """Lista todos os alunos cadastrados."""
    conn = create_connection()
    if conn is None:
        return

    alunos = execute_read_query(conn, "SELECT * FROM alunos")
    conn.close()

    if not alunos:
        print("\n Nenhum aluno cadastrado.\n")
        return

    print("\n Lista de Alunos:\n")
    for a in alunos:
        print(f"ID: {a['id']} | Matrícula: {a['matricula']} | Nome: {a['nome']} | Turma ID: {a['turma_id'] if a['turma_id'] else 'N/A'}")
    print()
def criar_aluno():
    """Cria um novo aluno no banco de dados."""
    conn = create_connection()
    if conn is None:
        return

    nome = input("\n Nome do Aluno: \n")
    matricula = input("\n Matrícula: \n")
    turma_id_str = input("\n ID da Turma (deixe vazio se não houver): \n")
    turma_id = int(turma_id_str) if turma_id_str.isdigit() else None
    check_query = "SELECT id FROM alunos WHERE matricula = ?"
        if execute_read_query(conn, check_query, (matricula,)):
            print("\n Matrícula já cadastrada.\n")
            conn.close()
            return
    
        insert_query = "INSERT INTO alunos (nome, matricula, turma_id) VALUES (?, ?, ?)"
        aluno_id = execute_query(conn, insert_query, (nome, matricula, turma_id))
        
        conn.close()
        
        if aluno_id:
            print(f"Aluno '{nome}' (ID: {aluno_id}) adicionado com sucesso!\n")
        else:
            print(f"Erro ao adicionar aluno '{nome}'.")

def ler_alunos():
    """Exibe a lista de todos os alunos."""
    listar_alunos()

def ler_um_aluno():
    """Exibe os detalhes de um aluno específico, incluindo notas."""
    conn = create_connection()
    if conn is None:
        return

    id_aluno_str = input("\n Digite o ID do aluno: \n")
    if not id_aluno_str.isdigit():
        print(" ID inválido.\n")
        conn.close()
        return
    id_aluno = int(id_aluno_str)
    
    aluno = buscar_aluno_por_id(conn, id_aluno)

    if aluno:
        print("\n Detalhes do Aluno:")
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Turma ID: {aluno['turma_id'] if aluno['turma_id'] else 'N/A'}")

        notas_query = "SELECT disciplina, valor FROM notas WHERE aluno_id = ?"
        notas = execute_read_query(conn, notas_query, (id_aluno,))

        if notas:
            print("\nNotas:")
            for nota in notas:
                print(f"  - Disciplina: {nota['disciplina']}, Nota: {nota['valor']:.2f}")
        else:
            print("\n O aluno ainda não possui notas cadastradas. \n")
        print()
    else:
        print("\n Aluno não encontrado.\n")
    
    conn.close()
def atualizar_aluno():
    """Atualiza os dados de um aluno existente, incluindo notas."""
    conn = create_connection()
    if conn is None:
        return

    listar_alunos()
    id_aluno_str = input("Digite o ID do aluno que deseja atualizar: ")
    if not id_aluno_str.isdigit():
        print(" ID inválido.\n")
        conn.close()
        return
    id_aluno = int(id_aluno_str)
    
    aluno = buscar_aluno_por_id(conn, id_aluno)

    if not aluno:
        print("\n Aluno não encontrado.\n")
        conn.close()
        return

    print(f"Editando: {aluno['nome']}")
    
    novo_nome = input(f"Novo nome (Atual: {aluno['nome']}): ") or aluno["nome"]
    nova_matricula = input(f"Nova matrícula (Atual: {aluno['matricula']}): ") or aluno["matricula"]
    
    nova_turma_id_str = input(f"Novo ID da Turma (Atual: {aluno['turma_id'] if aluno['turma_id'] else 'N/A'}): ")
    nova_turma_id = int(nova_turma_id_str) if nova_turma_id_str.isdigit() else None
    
    update_aluno_query = "UPDATE alunos SET nome = ?, matricula = ?, turma_id = ? WHERE id = ?"
    execute_query(conn, update_aluno_query, (novo_nome, nova_matricula, nova_turma_id, id_aluno))

    while True:
        print("\n Opções de Notas: \n")
        print("1. Adicionar Nota")
        print("2. Editar Nota")
        print("3. Concluir Edição de Aluno")
        op = input("Escolha uma opção: ")

        if op == "1":
            disciplina = input("Disciplina: ")
            valor_str = input("Nota (0.0 a 10.0): ")

            if not valor_str.replace('.', '', 1).isdigit():
                print("Valor de nota inválido. Use números.\n")
                continue

            valor = float(valor_str)

            nota_query = "INSERT INTO notas (aluno_id, disciplina, valor) VALUES (?, ?, ?)"
            execute_query(conn, nota_query, (id_aluno, disciplina, valor))
            print(f"Nota de {disciplina} adicionada com sucesso.")
        elif op == "2":
            disciplina = input("Disciplina que deseja editar: ")
            valor_str = input("Novo valor da nota (0.0 a 10.0): ")

            if not valor_str.replace('.', '', 1).isdigit():
                print("Valor de nota inválido. Use números.\n")
                continue

            valor = float(valor_str)

            nota_query = "UPDATE notas SET valor = ? WHERE aluno_id = ? AND disciplina = ?"
            execute_query(conn, nota_query, (valor, id_aluno, disciplina))
            
            print(f"Nota de {disciplina} editada com sucesso.")

        elif op == "3":
            break
            
        else:
            print("Opção inválida.")


    conn.close()
    print("Aluno atualizado com sucesso!\n")



