from arquivos import carregamentodedados, salvamentodedados, id_dados

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
      
