from arquivos import carregamentodedados, salvamentodedados, id_dados

def buscar_IdProfessor(professores, id_professor):
  for professor in professores:
    if professor["id"] == id_professor:
      return professor
  return None
def listar_professores(professores):
    if not professores:
        print("\n Nenhum professor cadastrado.\n")
        return
    print("\n Lista de Professores: \n")
    for p in professores:
        print(f"ID: {p['id']} | Matrícula: {p['matricula']} | Nome: {p['nome']} | Disciplina: {p['disciplina']
    print()
 def criar_professor():
    professores = carregaramentodedados("professores")
    nome = input("\n Nome do Professor: \n ")
    matricula = input(" \n Matrícula: \n ")
    disciplina = input(" \n Disciplina ministrada: \n")
    if any(p["matricula"] == matricula for p in professores):
        print("\n Matrícula já cadastrada.\n")
        return
    professor = {
        "id": id_dados(professores),
        "nome": nome,
        "matricula": matricula,
        "disciplina": disciplina,
    }
        professores.append(professor)
    salvamentodedados(professores, "professores")
    print(f"Professor '{nome}' (ID: {professor['id']}) adicionado com sucesso!\n")
def ler_professores():
    professores = carregaramentodedados("professores")
    listar_professores(professores)
def ler_um_professor():
    professores = carregaramentodedados("professores")
    if not professores:
        print("\n Nenhum professor cadastrado.\n")
        return
    id_digitado = input("Digite o ID do professor: ")
    if not id_digitado.isdigit():
        print("\n ID inválido. Digite apenas números.\n")
        return
    id_professor = int(id_digitado)
    professor = buscar_IdProfessor(professores, id_professor)
    if professor:
        print("\nDetalhes do Professor:")
        print(f"ID: {professor['id']}")
        print(f"Nome: {professor['nome']}")
        print(f"Matrícula: {professor['matricula']}")
        print(f"Disciplina: {professor['disciplina']}\n")
    else:
        print("\n Professor não encontrado.\n")
def atualizar_professor():
    professores = carregaramentodedados("professores")
    listar_professores(professores)

    id_digitado = input("\n Digite o ID do professor que deseja atualizar: ")
    if not id_digitado.isdigit():
        print("\n ID inválido. Digite apenas números.\n")
        return
    id_professor = int(id_digitado)
    professor = buscar_IdProfessor(professores, id_professor)
    if not professor:
        print("\n Professor não encontrado.\n")
        return
    print(f"Editando: {professor['nome']}")
    nome = input(f"Novo nome (Atual: {professor['nome']}): ")
    matricula = input(f"Nova matrícula (Atual: {professor['matricula']}): ")
    disciplina = input(f"Nova disciplina (Atual: {professor['disciplina']}): ")
    if nome:
        professor["nome"] = nome
    if matricula:
        professor["matricula"] = matricula
    if disciplina:
        professor["disciplina"] = disciplina
    salvamentodedados(professores, "professores")
    print("\n Professor atualizado com sucesso!\n")
def deletarprofessor():
    professores = carregaramentodedados("professores")
    listar_professores(professores)
    id_digitado = input("Digite o ID do professor que deseja excluir: ")
    if not id_digitado.isdigit():
        print("\n ID inválido. Digite apenas números.\n")
        return
    id_professor = int(id_digitado)
    professor = buscar_IdProfessor(professores, id_professor)

    if not professor:
        print("Professor não encontrado.\n")
        return
    professores.remove(professor)
    salvamentodedados(professores, "professores")
    print(f"Professor '{professor['nome']}' removido com sucesso!\n")

