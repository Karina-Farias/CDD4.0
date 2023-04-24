Nome = []
Senha = []


for x in range(1):
    Nome.append(input("Cadastre um nome:"))
    Senha.append(int(input("Cadastre uma senha:")))
NovoNome = input("Digite o nome:")
NovaSenha = int(input("Digite a senha:"))

for y in range(1):
    if Nome[y] == NovoNome and Senha[y] == NovaSenha:
        print("Acesso Liberado")

    else:
        print("Nome ou senha incorreta! Tente Novamente!")
