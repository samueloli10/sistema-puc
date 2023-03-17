nome_aluno = " "
codigo_aluno = 0
opcao = 1

while opcao != 0:
    print("\n\n-----MENU-----")
    print("1 - INCLUIR")
    print("2 - LISTAR")
    print("3 - ALTERAR")
    print("4 - EXCLUIR")
    print("0 - SAIR")

    while True:
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                nome_aluno = input("\n\nDigite o nome do aluno: ")
                codigo_aluno = input("Digite o código do aluno: ")
                print("\n\n")
            elif opcao == 2:
                print("\n\nO nome do aluno é ", nome_aluno)
                print("O código do aluno é ", codigo_aluno, "\n\n")
            elif opcao == 3:
                nome_aluno = input("\n\nDigite o novo nome do aluno: ")
                codigo_aluno = input("Digite o novo código do aluno:")
                print("\n\n")
            elif opcao == 4:
                print("\n\n")
                nome_aluno = " "
                codigo_aluno = 0
                print("\n\n")
            elif opcao == 0:
                print("\n\nVocê escolheu sair.\n\n")
                break
            else :
                print("\n\nDigite uma opção válida.")
                break
            break
        except ValueError: 
            print("\n\nDigitou um valor inválido.\n\n")