numero = int(input("Digite um número:"))

if numero == 0:
    print("Digite um número diferente de zero!")

elif numero > 0:
    if numero % 2 == 0:
        print(numero, "é par positivo! ")
    else:
        print(numero, "é impar positivo! ")

else:
    if numero % 2 == 0:
        print(numero,"é par negativo!")
    else:
        print(numero,"é impar negativo!")