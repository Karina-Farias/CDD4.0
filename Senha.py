
contador = 0

while contador < 3:
    senha = input("Digite sua senha:")
    senhaCerta = "12345678"
    if senha == senhaCerta:
        print("Bem Vindo")
        break

    else:
        contador = contador + 1
    if contador == 3:
        print("Senha Bloqueada!")