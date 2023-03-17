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
                print("\n")
                break
            elif opcao == 2:
                print(f'\nNome do aluno: {nome_aluno}')
                print(f'Código do aluno: {codigo_aluno}\n')
                break
            elif opcao == 3:
                nome_aluno = input("\nDigite o novo nome do aluno: ")
                codigo_aluno = input("Digite o novo código do aluno:")
                print("\n")
                break
            elif opcao == 4:
                nome_aluno = " "
                codigo_aluno = 0
                break
            elif opcao == 0:
                print("\n*** Você escolheu sair. ***\n")
                break
            else :
                print("\n*** Digite uma opção válida! ***\n")
        except ValueError: 
            print("\n*** Digitou um valor inválido. ***\n")