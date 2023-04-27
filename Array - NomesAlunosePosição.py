qtdAluno = int(input("Quantidade de alunos da turma:"))

lista_alunos = []
for i in range(qtdAluno):
    lista_alunos.append(input("Digite o nome do Aluno:"))

#   A forma certa em outras Linguagem:
#           for x in range(qtdAluno):
#               print(lista_alunos[x]

for x in range(qtdAluno):
    print(lista_alunos[x],x)
