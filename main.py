opcao_principal = ' '
lista_opcoes = ['Estudantes', 'Professores', 'Disciplinas', 'Turmas', 'Matrículas', 'Sair' ]
lista_nome_estudantes = []

def create():
    print("\n===== INCLUSÃO =====")
    lista_nome_estudantes.append(input("Nome do estudante: "))

def read(lista_nome_estudantes):
    if len(lista_nome_estudantes) != 0:
        print("\n--- LISTA DE ESTUDANTES: ---")
        for nome in lista_nome_estudantes:
            print(nome)
        input("\nPressione ENTER para continuar...")
    else:
        print("\n***** NÃO HÁ ESTUDANTES CADASTRADOS. *****\n")
        input("\nPressione ENTER para continuar...")

while opcao_principal != 6:
    print("---- MENU PRINCIPAL ----")
    print("(1) - Gerenciar estudantes.\n(2) - Gerenciar professores.\n(3) - Gerenciar disciplinas.\n(4) - Gerenciar turmas.\n(5) - Gerenciar matrículas.\n(6) - Sair")
    try:
        opcao_principal = int(input("Digite o número da opção: "))
    except ValueError:
        print("\n***** VALOR INVÁLIDO. *****\n")
    except:
        print("\n***** OCORREU UM ERRO. *****\n")
    opcao_operacoes = ' '
    if opcao_principal == 1:
        while opcao_operacoes != 5:
            print(f'\n***** [{lista_opcoes[opcao_principal - 1]}] MENU DE OPERAÇÕES *****')
            print("(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n(5) Voltar ao menu principal.\n")
            opcao_operacoes = int(input("Digite o número da opção: "))
            if opcao_principal == 1 and opcao_operacoes == 1:
                create()
            elif opcao_principal == 1 and opcao_operacoes == 2:
                read(lista_nome_estudantes)
            elif opcao_operacoes == 5:
                print("\n ***** VOLTANDO... *****\n")
                opcao_principal = 0
            else:
                print("\n***** EM DESENVOLVIMENTO. *****\n")
                input("\nPressione ENTER para continuar...")
    elif opcao_principal == 6:
        print("\n***** SAINDO... *****\n")
        break
    elif opcao_principal == 2 or opcao_principal == 3 or opcao_principal == 4 or opcao_principal == 5:
        print("\n***** EM DESENVOLVIMENTO. *****\n")
        input("\nPressione ENTER para continuar...")
    else:
        print("\n***** DIGITE UMA OPÇÃO VÁLIDA. *****\n")
        input("\nPressione ENTER para continuar...")
