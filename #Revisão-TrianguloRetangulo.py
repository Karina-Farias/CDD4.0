Menu = 0

while Menu != 100:

    Menu = int(input(        "\n"
                             "Selecione a opção:\n"
                             "1 - Área do triângulo\n"
                             "2 - Área do retângulo\n"
                             "3 - Sair\n"))

    if Menu == 1:
        BaseT = float(input("Digite o valor da base: "))
        AlturaT = float(input("Digite o valor da altura: "))

        AT = (BaseT * AlturaT)/2

        print("O Valor da área do triângulo é",AT)

    elif Menu == 2:
        BaseR = float(input("Digite o valor da base: "))
        AlturaR = float(input("Digite o valor da altura: "))

        AR = (BaseR * AlturaR)

        print("O Valor da área do triângulo é", AR)

    elif Menu != 1 and Menu != 2 and Menu != 3:
            print("Opção Inválida!")

    else:
        break