numeradorSoma = 0
denomidador = 10
i = 0

while i < denomidador:
    nota = float(input("Digite uma nota: "))

    numeradorSoma = numeradorSoma + nota
    i = i + 1

print("A média é: ", numeradorSoma/denomidador)