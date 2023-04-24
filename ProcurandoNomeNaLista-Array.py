qtdAluno = int(input("Quantidade de alunos da turma:"))

lista_alunos = []
for x in range(qtdAluno):
    lista_alunos.append(input("Digite o nome do Aluno:"))

pesquisa = input("Digite um nome para pesquisa:")
for y in range(qtdAluno):
    if pesquisa == lista_alunos[y]:
        print(y,lista_alunos[y])