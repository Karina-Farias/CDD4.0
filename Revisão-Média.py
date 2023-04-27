MediasdosAlunos = []
recalcular = "s"
while recalcular == "s":

    Nota1 = float(input("Digite Nota1:"))
    Nota2 = float(input("Digite Nota2:"))
    media = (Nota1+Nota2)/2

    MediasdosAlunos.append(media)

    if media >= 7:
        print("Aprovado")

    elif media >= 4:
        print("Recuperação")

    else:
        print("Reprovado!")

    recalcular = input("Deseja realizar novo cálculo? s/n: ")

print(MediasdosAlunos)