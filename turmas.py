from arquivos import carregamentodedados, salvamentodedados, id_dados

def buscarIdTurma(turmas, id_turma):
    for turma in turmas:
        if turma["id"] == id_turma:
            return turma
    return None


