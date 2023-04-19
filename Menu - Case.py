resp = 5
while resp != 6:

    Numero1 = float(input("Digite o primeiro número:"))
    Numero2 = float(input("Digite o segundo número:"))

    while True:
        resp = int(input("Selecione a operação:\n"
                             "1 - Soma\n"
                             "2 - Subtração\n"
                             "3 - Multiplicação\n"
                             "4 - Divisão\n"
                             "5 - Digite os números novamente\n"
                             "6 - Sair\n"))

        match resp:
            case 1:
                print(Numero1 + Numero2)

            case 2:
                print(Numero1 - Numero2)

            case 3:
                print(Numero1 * Numero2)

            case 4:
                print(Numero1 / Numero2)

            case 5:
                break

            case 6:
                resp = 6
                break