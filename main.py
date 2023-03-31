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
                print("\n***** DIGITE UMA OPÇÃO VÁLIDA. *****\n")
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
                    try: 
                        print(f"\n===== [ESTUDANTE] INCLUSÃO =====")  
                        codigo = int(input("Digite o código: "))
                        nome = input("Digite o nome: ")
                        cpf = input("Digite o CPF: ")
                        if verificar_dados(lista_estudantes, cpf) or verificar_dados(lista_estudantes, codigo):
                            continue
                        else:
                            dicionario = {'Código': codigo, 'Nome': nome, 'CPF': cpf}
                            lista_estudantes = create(lista_estudantes, dicionario)  
                    except ValueError:
                        print("\n***** VALOR INVÁLIDO. *****\n")
                        input("\nPressione ENTER para continuar...")
                    except:
                        print("\n***** OCORREU UM ERRO. *****\n")
                        input("\nPressione ENTER para continuar...")
                elif opcao_operacao == 2:
                    print("\n===== [ESTUDANTE] LISTAGEM =====\n")
                    read(lista_estudantes)
                elif opcao_operacao == 4:
                    print("\n===== [ESTUDANTE] EXCLUIR =====\n")
                    codigo = int(input("Digite o código: "))
                    lista_estudantes = delete(lista_estudantes, codigo)
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

def verificar_dados(lista, valor_procurado):
    for dicionario in lista:
        for chave, valor in dicionario.items():
            if valor_procurado == valor:
                print(f"\n===== VERIFICAÇÃO =====")  
                print(f'O {chave}: {valor} está presente no cadastro:\n{dicionario}\n\nOperação cancelada...') 
                return True
    return False

def create(lista, dicionario):
    lista.append(dicionario)
    print("\nCadastro concluído...")
    return lista
             
def read(lista):
    if len(lista) != 0:
        for dicionario in lista:
            for chave, valor in dicionario.items():
                print(f'{chave}: {valor}')    
            print("\n==================\n")             
        input("\nPressione ENTER para continuar...")    
    else:
        print("\n***** NÃO HÁ ESTUDANTES CADASTRADOS. *****\n")
        input("\nPressione ENTER para continuar...")
        
def update():
    return

def delete(lista, valor):
    for dicionario in lista:
        if valor in dicionario.values():
            lista.remove(dicionario)
            print("\nCadastro excluído...")
            return lista
    print("\nNão existe cadastro com esse valor...")
    return lista
inicio() #inicio do sistema