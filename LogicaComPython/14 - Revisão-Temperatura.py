while True:

    TemperaturaF = int(input("Digite a temperatura em Fahrenheit: "))
    C = ((TemperaturaF - 32)/9)*5
    print("A temperatura em Celsius é:",C)

    Resposta = input("Deseja continuar? ")
    if Resposta == "não":
        break
