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
  if os.path.exists(arquivo):
     with open(arquivo, "r", encoding="utf-8") as f:
         conteudo = f.read().strip() 
         if not conteudo:
             print(f"O arquivo {arquivo} está vazio. Retornando lista vazia.")
             return []
         dados = json.loads(conteudo)
         return dados
 print(f"O arquivo {arquivo} não foi encontrado. Criando lista vazia.")
 return []
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
  
