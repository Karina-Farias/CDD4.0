while True:

    n = int(input("Digite um número: "))

    if n == 0:
        print("Digite um número diferente de zero!")

    elif n > 0:
        print("Número positivo! ")

    else:
        print("Número Negativo!")

    Resposta = input("Deseja continuar? ")
    if Resposta == "não":
        break