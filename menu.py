from crud_menu import menu_crud_alunos, menu_crud_professores, menu_crud_turmas
from relatorios import exibir_menu_relatorios

def exibir_menu():
   while True:
        print("\n========== SISTEMA DE GESTÃO ESCOLAR COMUNITÁRIA ==========")
        print("1. Gerenciar Alunos (CRUD)")
        print("2. Gerenciar Professores (CRUD)")
        print("3. Gerenciar Turmas (CRUD)")
        print("4. Relatórios")
        print("5. Sair")
        print("=============================================================")

        opcao = input("Escolha uma opção: ")

      
