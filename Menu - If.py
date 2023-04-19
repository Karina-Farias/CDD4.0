operacao = 0

while operacao != 6:

    Numero1 = float(input("Digite o primeiro número:"))
    Numero2 = float(input("Digite o segundo número:"))


    operacao = int(input("Selecione a operação:\n"
                             "1 - Soma\n"
                             "2 - Subtração\n"
                             "3 - Multiplicação\n"
                             "4 - Divisão\n"
                             "5 - Digite os números novamente\n"
                             "6 - Sair\n"))

    if operacao == 1:
        print(Numero1 + Numero2)

    elif operacao == 2:
        print(Numero1 - Numero2)

    elif operacao == 3:
        print(Numero1 * Numero2)

    elif operacao == 4:
        print(Numero1 / Numero2)

    elif operacao ==5:
        continue

    else:
        break