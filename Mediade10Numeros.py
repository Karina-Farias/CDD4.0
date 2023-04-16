numerador = 0
denomidador =0

for i in range(10):
    nota = float(input("Digite uma nota:"))

    numerador = numerador + nota
    denomidador = denomidador + 1

print("A média é: ", numerador/denomidador)
