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
            input("\nPressione ENTER para continuar...");
        except:
            print("\n***** OCORREU UM ERRO. *****\n")
            input("\nPressione ENTER para continuar...")

def menu_operacoes(opcao_principal):
    lista_opcoes = ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA', 'SAIR1' ]
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
                        print(f"\n===== [ESTUDANTE] INCLUIR =====")  
                        codigo = int(input("Digite o código: "))
                        nome = input("Digite o nome: ")
                        cpf = input("Digite o CPF: ")                  
                        if verificar_dados(lista_estudantes, codigo) is None:
                            if verificar_dados(lista_estudantes, cpf) is None:
                                dicionario_encontrado = {'Código': codigo, 'Nome': nome, 'CPF': cpf}
                                create(lista_estudantes, dicionario_encontrado)
                                print("\nCadastro realizado com sucesso...")
                            else:
                                print(f"\n===== ERRO =====")  
                                print(f'O CPF: {cpf} está presente no cadastro:\n{verificar_dados(lista_estudantes, cpf)}\n\nOperação cancelada...')  
                        else:
                            print(f"\n===== ERRO =====")  
                            print(f'O código: {codigo} está presente no cadastro:\n{verificar_dados(lista_estudantes, codigo)}\n\nOperação cancelada...')
                    except ValueError:
                        print("\n***** VALOR INVÁLIDO. *****\n")
                        input("\nPressione ENTER para continuar...")
                    except:
                        print("\n***** OCORREU UM ERRO. *****\n")
                        input("\nPressione ENTER para continuar...")
                elif opcao_operacao == 2:
                    print("\n===== [ESTUDANTE] LISTAR =====\n")
                    if read_all(lista_estudantes) == False:
                        print("\n***** NÃO HÁ ESTUDANTES CADASTRADOS. *****\n")
                        input("\nPressione ENTER para continuar...")
                    else:
                        input("\nPressione ENTER para continuar...")
                elif opcao_operacao == 3:
                    try:
                        print("\n===== [ESTUDANTE] ATUALIZAR =====\n")
                        codigo = int(input("BUSCAR: Digite o código: "))
                        dicionario_encontrado = verificar_dados(lista_estudantes, codigo)
                        if dicionario_encontrado is None:
                            print("\nCadastro não encontrado...")
                        else:
                            print("\nCadastro encontrado...\n")
                            read_one(dicionario_encontrado)  
                            codigo = int(input("Digite o novo código: "))
                            nome = input("Digite o novo nome: ")
                            cpf = input("Digite o novo CPF: ")
                            if verificar_dados(lista_sem_repetir(lista_estudantes, dicionario_encontrado), codigo) is None :
                                if verificar_dados(lista_sem_repetir(lista_estudantes, dicionario_encontrado), cpf) is None:
                                    dicionario_novo = {'Código': codigo, 'Nome': nome, 'CPF': cpf}
                                    update(lista_estudantes, dicionario_novo, dicionario_encontrado)
                                    print("\nCadastro atualizado com sucesso...")
                                else:
                                    print(f"\n===== ERRO =====")  
                                    print(f'O CPF: {cpf} não pode ser utilizado.\n\nOperação cancelada...')  
                            else:
                                print(f"\n===== ERRO =====")  
                                print(f'O Código: {codigo} não pode ser utilizado.\n\nOperação cancelada...')  
                    except ValueError:
                        print("\n***** VALOR INVÁLIDO. *****\n")
                        input("\nPressione ENTER para continuar...")
                    except:
                        print("\n***** OCORREU UM ERRO. *****\n")
                        input("\nPressione ENTER para continuar...")
                elif opcao_operacao == 4:
                    try: 
                        print("\n===== [ESTUDANTE] EXCLUIR =====\n")
                        codigo = int(input("BUSCAR: Digite o código: "))
                        if verificar_dados(lista_estudantes, codigo) is None:
                            print("\nNão existe cadastro com esse valor...")
                        else:
                            delete(lista_estudantes, verificar_dados(lista_estudantes, codigo))
                            print("\nCadastro excluído com sucesso...")
                    except ValueError:
                        print("\n***** VALOR INVÁLIDO. *****\n")
                        input("\nPressione ENTER para continuar...")
                    except:
                        print("\n***** OCORREU UM ERRO. *****\n")
                        input("\nPressione ENTER para continuar...")
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
        for valor in dicionario.values():
            if valor_procurado == valor:
                return dicionario
    return None

def lista_sem_repetir(lista, dicionario_encontrado):
    lista_sem_repetidos = [] 
    for dicionario in lista:
        if dicionario == dicionario_encontrado:
            return lista_sem_repetidos
        lista_sem_repetidos.append(dicionario)
        return lista_sem_repetidos

def create(lista, dicionario):
    lista.append(dicionario)
             
def read_all(lista):
    if len(lista) != 0:
        for dicionario in lista:
            for chave, valor in dicionario.items():
                print(f'{chave}: {valor}')    
            print("\n==================\n") 
        return True              
    else:
        return False

def read_one(dicionario):
    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')   
    print("\n==================\n") 

def update(lista, dicionario_novo, dicionario_atual):
    delete(lista, dicionario_atual)
    create(lista, dicionario_novo)

def delete(lista, dicionario):
    lista.remove(dicionario)

inicio() #inicio do sistema