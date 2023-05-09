numerador = 0
denominador = 4

for i in range(4):
    nota = float(input("Digite uma nota:"))

    numerador = numerador + nota
    media = numerador/denominador

print("A média é: ",media)
