from alunos import criar_aluno, ler_alunos, ler_um_aluno, atualizar_aluno, deletar_aluno
from professores import criar_professor, ler_professores, ler_um_professor, atualizar_professor, deletar_professor
from turmas import criar_turma, ler_turmas, ler_uma_turma, atualizar_turma, deletar_turma

def menu_crud_alunos():
    while True:
        print("\n========== GERENCIAR ALUNOS ==========")
        print("1. Cadastrar Aluno")
        print("2. Listar Todos os Alunos")
        print("3. Buscar Aluno por ID")
        print("4. Atualizar Aluno")
        print("5. Excluir Aluno")
        print("6. Voltar ao Menu Principal")
        print("======================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_aluno()
        elif opcao == "2":
            ler_alunos()
        elif opcao == "3":
            ler_um_aluno()
        elif opcao == "4":
            atualizar_aluno()
        elif opcao == "5":
            deletar_aluno()
        elif opcao == "6":
            break
        else:
            print(" Opção inválida, Tente novamente.\n")
