recalcular = "s"
while recalcular == "s":

    nota1 = float(input("Nota 1A:"))
    while nota1 < 0 or nota1 > 10:
        print("Digite uma nota de 0 e 10")
        nota1 = float(input())


    nota2 = float(input("Nota 2A:"))

    while nota2 < 0 or nota2 > 10:
        print("Digite uma nota entre 0 e 10")
        nota2 = float(input())

    media = (nota1 + nota2) / 2
    print(media)

    recalcular = input("Deseja realizar novo cálculo? s/n")
