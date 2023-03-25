# NOME: SAMUEL DE OLIVEIRA RÊGO
# CURSO: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

"""
def menu_principal():

Essa função implementa um loop que imprime um MENU PRINCIPAL com várias opções e solicita ao 
usuário que escolha uma delas.

Se a entrada do usuário for um número inteiro entre 1 e 6, a função retorna esse número. 
Caso contrário, a função exibe uma mensagem de erro apropriada e solicita que o usuário 
insira uma opção válida. Se houver uma exceção, a função exibe uma mensagem de erro genérica.
"""
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
"""
def menu_operacoes(opcao_principal):

Essa função é responsável por exibir o menu de operações para um determinado tipo de entidade, 
como estudantes, professores, disciplinas, etc. Recebe como parâmetro a opção principal selecionada 
pelo usuário no menu principal, para exibir o nome da entidade correta no menu de operações.

A função tem um loop infinito para manter o menu de operações sendo exibido até que o usuário 
selecione uma opção válida (1 a 5). Dentro do loop, são exibidas as opções do menu de operações e 
a opção selecionada pelo usuário é lida do teclado e validada. Se a opção digitada não estiver dentro 
do intervalo de 1 a 5, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.

Se ocorrer uma exceção do tipo ValueError (por exemplo, se o usuário digitar uma letra em vez de um número), 
uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente. Se ocorrer uma exceção de outro tipo,
uma mensagem de erro genérica é exibida e o usuário é solicitado a digitar novamente.

A função retorna a opção selecionada pelo usuário.
"""
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
"""
def inicio(): 

Dentro do loop principal, um menu de opções é apresentado na tela por meio da chamada 
da função menu_principal(). Se o usuário selecionar a opção 1, um novo loop é iniciado 
para apresentar as opções do menu de operações. Esse menu é apresentado na tela pela 
função menu_operacoes(), que retorna a opção selecionada pelo usuário. Se o usuário 
selecionar a opção 1 (criar estudante), a função create_estudante() é chamada, passando 
a lista nome_estudante como argumento. Se o usuário selecionar a opção 2 (ler estudante), 
a função read_estudante() é chamada, também passando a lista nome_estudante como argumento. 
Se o usuário selecionar a opção 5 (voltar ao menu principal), uma mensagem é exibida na tela 
e o loop de operações é interrompido com o comando break. Se o usuário selecionar outra opção 
que não seja 1, 2 ou 5, uma mensagem é exibida na tela indicando que essa opção ainda está em 
desenvolvimento.

Se o usuário selecionar a opção 6 (sair) no menu principal, uma mensagem é exibida na tela e 
o loop principal é interrompido com o comando break. Se o usuário selecionar outra opção que 
não seja 1 ou 6, uma mensagem é exibida na tela indicando que essa opção ainda está em desenvolvimento.
"""
def inicio(): 
    nome_estudante = []
    opcao_principal = ' '
    while opcao_principal != 6:
        opcao_principal = menu_principal()
        if opcao_principal == 1:
            opcao_operacao = ' '
            while opcao_operacao != 5:
                opcao_operacao = menu_operacoes(opcao_principal)
                if opcao_operacao == 1:
                    create_estudante(nome_estudante)
                elif opcao_operacao == 2:
                    read_estudante(nome_estudante)

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
"""
def create_estudante(nome_estudante):

Esse bloco de código define uma função chamada create_estudante que recebe uma lista vazia 
chamada nome_estudante como parâmetro. A função tem a finalidade de adicionar um novo nome 
de estudante à lista.

Na primeira linha da função, é exibida uma mensagem com o título "INCLUSÃO". Em seguida, a 
função solicita que o usuário insira o nome do estudante utilizando a função input do Python, 
que permite a entrada de dados via teclado. O valor inserido pelo usuário é adicionado à lista 
nome_estudante utilizando o método append().
"""
def create_estudante(nome_estudante):
    print("\n===== INCLUSÃO =====")
    nome_estudante.append(input("Nome do estudante: "))
"""
def read_estudante(nome_estudante):

A função read_estudante recebe como parâmetro uma lista nome_estudante contendo o nome dos estudantes 
cadastrados. Se a lista não estiver vazia, a função imprime os nomes dos estudantes cadastrados usando 
um loop for. Caso contrário, a função imprime uma mensagem informando que não há estudantes cadastrados. 
Em ambos os casos, a função espera que o usuário pressione ENTER para continuar. Essa função serve para 
listar os estudantes cadastrados no sistema.
"""
def read_estudante(nome_estudante):
    if len(nome_estudante) != 0:
        print("\n--- LISTA DE ESTUDANTES: ---")
        for nome in nome_estudante:
            print(nome)
        input("\nPressione ENTER para continuar...")
    else:
        print("\n***** NÃO HÁ ESTUDANTES CADASTRADOS. *****\n")
        input("\nPressione ENTER para continuar...")
    
inicio() #inicio do sistema