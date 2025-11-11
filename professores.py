from arquivos import carregamentodedados, salvamentodedados, id_dados

def buscar_IdProfessor(professores, id_professor):
  for professor in professores:
    if professor["id"] == id_professor:
      return professor
  return None
