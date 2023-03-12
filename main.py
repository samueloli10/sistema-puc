nome_aluno = " "
codigo_aluno = 0

print("-----MENU-----")
print("1 - INCLUIR")
print("2 - LISTAR")
print("3 - ALTERAR")
print("4 - EXCLUIR")
print("0 - SAIR")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    nome_aluno = input("Digite o nome do aluno: ")
    codigo_aluno = input("Digite o código do aluno: ")
elif opcao == 2:
    print("O nome do aluno é ", nome_aluno)
    print("O código do alunoe é ", codigo_aluno)
elif opcao == 3:
    nome_aluno = input("Digite o novo nome do aluno: ")
    codigo_aluno = input("Digite o novo código do aluno:")
elif opcao == 4:
    nome_aluno = " "
    codigo_aluno = 0
else :
    print("Opção invalida!")
    
