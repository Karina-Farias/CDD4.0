operacao = 0

def somar(N1,N2):
    print(N1+N2)

def subtracao(N1,N2):
    print(N1-N2)

def multiplicacao(N1,N2):
    print(N1*N2)

def divisao(N1,N2):
    print(N1/N2)

while operacao != 6:

    operacao = int(input("Selecione a operação:\n"
                             "1 - Soma\n"
                             "2 - Subtração\n"
                             "3 - Multiplicação\n"
                             "4 - Divisão\n"
                             "5 - Sair\n"))
    if operacao == 5:
        break

    N1 = float(input("Digite o primeiro número:"))
    N2 = float(input("Digite o segundo número:"))

    if operacao == 1:
        somar(N1,N2)

    elif operacao == 2:
        subtracao(N1,N2)

    elif operacao == 3:
        multiplicacao(N1,N2)

    else:
        divisao(N1,N2)
