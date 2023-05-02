numerador = 0
denomidador = 4

for i in range(4):
    nota = float(input("Digite uma nota:"))

    numerador = numerador + nota
    media = numerador/denomidador

print("A média é: ",media)