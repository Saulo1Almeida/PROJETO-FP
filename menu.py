from crud_menu import menu_crud_alunos, menu_crud_professores, menu_crud_turmas
from relatorios import exibir_menu_relatorios
from database import initialize_db

def exibir_menu():
    initialize_db() 
    
    while True:
        print("\n========== SISTEMA DE GESTÃO ESCOLAR  ==========")
        print("1. Gerenciar Alunos (PROFESSORES/DIREÇÃO) ")
        print("2. Gerenciar Professores (DIREÇÃO) ")
        print("3. Gerenciar Turmas (DIREÇÃO) ")
        print("4. Relatórios")
        print("5. Sair")
        print("=============================================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_crud_alunos()
        elif opcao == "2":
            menu_crud_professores()
        elif opcao == "3":
            menu_crud_turmas()
        elif opcao == "4":
            exibir_menu_relatorios()
        elif opcao == "5":
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida,Tente novamente.\n")


