from arquivos import carregaramentodedados, salvamentodedados, id_dados

def buscar_IdProfessor(alunos, id_aluno):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            return aluno
    return None
def listar_alunos(alunos):
    if not alunos:
        print("\n Nenhum aluno cadastrado.\n")
        return
    print("\n Lista de Alunos:\n")
    for a in alunos:
        print(f"ID: {a['id']} | Matrícula: {a['matricula']} | Nome: {a['nome']} | Turma ID: {a['turma_id']}")
    print()
def criar_aluno():
    alunos = carregaramentodedados("\nalunos\n")
    nome = input("\n Nome do Aluno: \n")
    matricula = input("\n Matrícula: \n")
    turma_id = input("\n ID da Turma (deixe vazio se não houver): \n")
    if any(a["matricula"] == matricula for a in alunos):
        print("\n Matrícula já cadastrada.\n")
        return
    aluno = {
        "id":  id_dados(alunos),
        "nome": nome,
        "matricula": matricula,
        "turma_id": int(turma_id) if turma_id.isdigit() else None,
        "notas": []
    }
    alunos.append(aluno)
    salvamentodedados(alunos, "\n alunos \n")
    print(f"Aluno '{nome}' (ID: {aluno['id']}) adicionado com sucesso!\n")
def ler_alunos():
    alunos = carregaramentodedados("alunos")
    listar_alunos(alunos)
def ler_um_aluno():
    alunos = carregaramentodedados("alunos")
    if not alunos:
        print("\n Nenhum aluno cadastrado.\n")
        return
    id_aluno_str = input("\n Digite o ID do aluno: \n")
    if not id_aluno_str.isdigit():
        print(" ID inválido.\n")
        return
    id_aluno = int(id_aluno_str)
    aluno = buscar_IdProfessor(alunos, id_aluno)
    if aluno:
        print("\n Detalhes do Aluno:")
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Turma ID: {aluno['turma_id'] if aluno['turma_id'] else 'N/A'}")
        if aluno['notas']:
            print("\nNotas:")
            for nota in aluno['notas']:
                print(f"  - Disciplina: {nota['disciplina']}, Nota: {nota['valor']:.2f}")
        else:
            print("\n O aluno ainda não possui notas cadastradas. \n")
        print()
    else:
        print("\n Aluno não encontrado.\n")
def atualizar_aluno():
    alunos = carregaramentodedados("alunos")
    listar_alunos(alunos)
    id_aluno_str = input("Digite o ID do aluno que deseja atualizar: ")
    if not id_aluno_str.isdigit():
        print(" ID inválido.\n")
        return
    id_aluno = int(id_aluno_str)
    aluno = buscar_IdProfessor(alunos, id_aluno)
    if not aluno:
        print("\n Aluno não encontrado.\n")
        return
    print(f"Editando: {aluno['nome']}")
    aluno["nome"] = input(f"Novo nome (Atual: {aluno['nome']}): ") or aluno["nome"]
    aluno["matricula"] = input(f"Nova matrícula (Atual: {aluno['matricula']}): ") or aluno["matricula"]
    nova_turma_id = input(f"Novo ID da Turma (Atual: {aluno['turma_id'] if aluno['turma_id'] else 'N/A'}): ")
    if nova_turma_id.isdigit():
        aluno["turma_id"] = int(nova_turma_id)
    while True:
        print("\n Opções de Notas: \n")
        print("1. Adicionar/Editar Nota")
        print("2. Concluir Edição de Aluno")
        op = input("Escolha uma opção: ")
        if op == "1":
            disciplina = input("Disciplina: ")
            valor_str = input("Nota (0.0 a 10.0): ")

            if not valor_str.replace('.', '', 1).isdigit():
                print("Valor de nota inválido. Use números.\n")
                continue
            valor = float(valor_str)
            nota_encontrada = False
            for nota in aluno['notas']:
                if nota['disciplina'].lower() == disciplina.lower():
                    nota['valor'] = valor
                    nota_encontrada = True
                    break    
            if not nota_encontrada:
                aluno['notas'].append({"disciplina": disciplina, "valor": valor})
            print(f"Nota de {disciplina} atualizada/adicionada com sucesso.")
        elif op == "2":
            break
        else:
            print("Opção inválida.")
    salvamentodedados(alunos, "alunos")
    print("Aluno atualizado com sucesso!\n")
def deletar_aluno():
    """Deleta um aluno existente pelo ID."""
    alunos = carregaramentodedados("alunos")
    listar_alunos(alunos)
    id_aluno_str = input("Digite o ID do aluno que deseja excluir: ")
    if not id_aluno_str.isdigit():
        print(" ID inválido.\n")
        return
    id_aluno = int(id_aluno_str)
    aluno = buscar_IdProfessor(alunos, id_aluno)
    if aluno:
        alunos.remove(aluno)
        salvamentodedados(alunos, "alunos")
        print(f"Aluno '{aluno['nome']}' removido com sucesso!\n")
    else:
        print("\n Aluno não encontrado.\n")
