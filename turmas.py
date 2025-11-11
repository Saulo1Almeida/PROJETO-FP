from arquivos import carregamentodedados, salvamentodedados, id_dados

def buscarIdTurma(turmas, id_turma):
    for turma in turmas:
        if turma["id"] == id_turma:
            return turma
    return None

def ler_turmas():
    turmas = carregaramentodedados("turmas")

    if not turmas:
        print("Nenhuma turma cadastrada.\n")
        return

    print("\nLista de Turmas:")
    for t in turmas:
        print(f"ID: {t['id']} | Nome: {t['nome']} | Professor ID: {t['professor_id']}")
    print()
    
def criar_turma():
    turmas = carregaramentodedados("turmas")
    
    nome = input("Digite o nome da turma: ")
    professor_id = input("ID do professor: ")
    
    turma = {
        "id": id_dados(turmas),
        "nome": nome,
        "professor_id": int(professor_id) if professor_id.isdigit() else None
    }

    turmas.append(turma)
    salvamentodedados(turmas, "turmas")
    print(f"Turma '{nome}' criada com sucesso!\n")


