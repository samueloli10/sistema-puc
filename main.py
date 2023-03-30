# NOME: SAMUEL DE OLIVEIRA RÊGO
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

def menu_principal():
    while True:
        print("---- MENU PRINCIPAL ----")
        print("(1) - Gerenciar estudantes.\n(2) - Gerenciar professores.\n(3) - Gerenciar disciplinas.\n(4) - Gerenciar turmas.\n(5) - Gerenciar matrículas.\n(6) - Sair")
        try:
            opcao = int(input("Digite o número da opção: "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("\n***** priDIGITE UMA OPÇÃO VÁLIDA. *****\n")
                input("\nPressione ENTER para continuar...")
        except ValueError:
            print("\n***** VALOR INVÁLIDO. *****\n")
            input("\nPressione ENTER para continuar...")
        except:
            print("\n***** OCORREU UM ERRO. *****\n")
            input("\nPressione ENTER para continuar...")

def menu_operacoes(opcao_principal):
    lista_opcoes = ['Estudantes', 'Professores', 'Disciplinas', 'Turmas', 'Matrículas', 'Sair' ]
    while True:
        print(f'\n***** [{lista_opcoes[opcao_principal - 1]}] MENU DE OPERAÇÕES *****')
        print("(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n(5) Voltar ao menu principal.\n")
        try:
            opcao = int(input("Digite o número da opção: "))
            if 1 <= opcao <= 5:
                return opcao
            else:
                print("\n***** DIGITE UMA OPÇÃO VÁLIDA. *****\n")
                input("\nPressione ENTER para continuar...")
        except ValueError:
            print("\n***** VALOR INVÁLIDO. *****\n")
            input("\nPressione ENTER para continuar...")
        except:
            print("\n***** OCORREU UM ERRO. *****\n")
            input("\nPressione ENTER para continuar...")

def inicio(): 
    lista_estudantes = []
    opcao_principal = ' '
    while opcao_principal != 6:
        opcao_principal = menu_principal()
        if opcao_principal == 1:
            opcao_operacao = ' '
            while opcao_operacao != 5:
                opcao_operacao = menu_operacoes(opcao_principal)
                if opcao_operacao == 1:
                    lista_estudantes = create_estudante(lista_estudantes)  
                elif opcao_operacao == 2:
                    read_estudante(lista_estudantes)
                elif opcao_operacao == 5:       
                    print("\n ***** VOLTANDO... *****\n")
                    break
                else:
                    print("\n***** EM DESENVOLVIMENTO. *****\n")
                    input("\nPressione ENTER para continuar...")
        elif opcao_principal == 6:
            print("\n***** SAINDO... *****\n")
            break
        else:
            print("\n***** EM DESENVOLVIMENTO. *****\n")
            input("\nPressione ENTER para continuar...")

def create_estudante(lista_estudantes):
    print("\n===== [ESTUDANTE] INCLUSÃO =====")
    while True:
        try:
            codigo = int(input("Digite o código: "))
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            dicionario_estudante = {'Código': codigo, 'Nome': nome, 'CPF': cpf}
            lista_estudantes.append(dicionario_estudante)
            return lista_estudantes
        except ValueError:
            print("\n***** VALOR INVÁLIDO. *****\n")
            input("\nPressione ENTER para continuar...")
        except:
            print("\n***** OCORREU UM ERRO. *****\n")
            input("\nPressione ENTER para continuar...")

def read_estudante(lista_estudantes):
    if len(lista_estudantes) != 0:
        print("\n===== [ESTUDANTE] LISTAGEM =====\n")
        for dicionario_estudante in lista_estudantes:
            for chave, valor in dicionario_estudante.items():
                print(f'{chave}: {valor}')    
            print("\n==================\n")             
        input("\nPressione ENTER para continuar...")    
    else:
        print("\n***** NÃO HÁ ESTUDANTES CADASTRADOS. *****\n")
        input("\nPressione ENTER para continuar...")
        
    

inicio() #inicio do sistema