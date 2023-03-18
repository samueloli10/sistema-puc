nome_aluno = " "
codigo_aluno = 0
opcao1 = ' '
opcao2 = ' '

while opcao1 != 0: 
    print("---- MENU PRINCIPAL ----")
    print("(1) - Gerenciar estudantes.")
    print("(2) - Gerenciar professores.")
    print("(3) - Gerenciar disciplinas.")
    print("(4) - Gerenciar turmas.")
    print("(5) - Gerenciar matrículas.")
    opcao1 = int(input("Digite a opção: "))
    while opcao2 != 0:
        print("\n\n-----MENU-----")
        print("1 - INCLUIR")
        print("2 - LISTAR")
        print("3 - ALTERAR")
        print("4 - EXCLUIR")
        print("0 - VOLTAR")
        while True:
            try:
                opcao2 = int(input("Digite a opção: "))
                if opcao1 == 1 and opcao2 == 1:
                    nome_aluno = input("\n\nDigite o nome do aluno: ")
                    codigo_aluno = input("Digite o código do aluno: ")
                    print("\n")
                    break
                elif opcao1 == 1 and opcao2 == 2:
                    print("\nO nome do aluno é ", nome_aluno)
                    print("O código do aluno é ", codigo_aluno, "\n")
                    break
                elif opcao1 == 1 and opcao2 == 3:
                    nome_aluno = input("\nDigite o novo nome do aluno: ")
                    codigo_aluno = input("Digite o novo código do aluno:")
                    print("\n")
                    break
                elif opcao1 == 1 and opcao2 == 4:
                    print("\n")
                    nome_aluno = " "
                    codigo_aluno = 0
                    print("\n")
                    break
                elif opcao1 == 1 and opcao2 == 0:
                    print("\n*** Você escolheu voltar. ***\n")
                    break
                else :
                    print("\n*** Digite uma opção válida! ***")
            except ValueError: 
                print("\n*** Digitou um valor inválido. ***\n")