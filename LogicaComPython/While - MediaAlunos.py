numerador_Soma = 0
denomidador_QtdAlunos = int(input("Quantos Alunos tem a turma:"))
i = 0

while i < denomidador_QtdAlunos:
    nota = float(input("Digite uma nota: "))

    numerador_Soma = numerador_Soma + nota
    i = i + 1

print("A média é: ", numerador_Soma/denomidador_QtdAlunos)
