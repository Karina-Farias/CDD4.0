numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_pares = []
numeros_impares = []
numeros_positivos = []
numeros_negativos = []
zeros = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

    if numero > 0:
        numeros_positivos.append(numero)
    elif numero < 0:
        numeros_negativos.append(numero)
    else:
        zeros.append(numero)

print("Números ímpares:", numeros_impares)
print("Números pares:", numeros_pares)
print("Números positivos:", numeros_positivos)
print("Números negativos:", numeros_negativos)
print("Zeros:", zeros)
