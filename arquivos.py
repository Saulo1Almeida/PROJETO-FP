import json
import os

arquivoalunos = "alunos.json"
arquivoprofessores = "professores.json"
arquivoturmas = "turmas.json"

def carregamentodedados(tipo):
  if tipo == "alunos":
    arquivo = arquivoalunos
  elif tipo == "professores":
    arquivo = arquivoprofessores
  elif tipo == "turmas":
    arquivo = arquivoturmas
  else:
    print(f" Tipo de dado desconhecido: {tipo}")
    return[]
