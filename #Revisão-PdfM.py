confirm = "SIM"
while confirm == "SIM":
    Frase = input("Digite seu nome ou uma frase :")
    for x in Frase:
        if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
            print(x, end="")
    print()
    confirm = input("Quer continuar?\nDigite SIM para continuar ou qualquer outra coisa para sair: ")
print("Programa encerrado")