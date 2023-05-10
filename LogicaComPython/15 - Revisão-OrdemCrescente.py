while True:

    n1 = input("Digite um número:")
    n2 = input("Digite outro número:")

    if n1 == n2:
        print("Digite Números Diferentes!")

    elif n1 < n2:
        print(n1,n2)

    else:
        print(n2, n1)

    Resposta = input("Deseja continuar? ")
    if Resposta == "não":
        break
