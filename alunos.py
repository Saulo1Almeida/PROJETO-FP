from arquivos import carregamentodedados, salvamentodedados, id_dados

def buscar_IdProfessor(alunos, id_aluno):
  for aluno in alunos:
    if aluno["id"] == id_aluno:
      return aluno
  return None
