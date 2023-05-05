while True:

    Base = float(input("Digite o valor da base: "))
    Altura = float(input("Digite o valor da altura: "))

    A = (Base * Altura)/2

    print("O Valor da área do triângulo é",A)

    Resposta = input("Deseja continuar? ")
    if Resposta == "não":
        break