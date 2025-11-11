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


