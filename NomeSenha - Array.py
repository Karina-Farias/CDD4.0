Nome = []
Senha = []

for x in range(5):
    Nome.append(input("Digite um nome:"))
    Senha.append(int(input("Digite uma senha:")))

for y in range(5):
    print("Posição:",y,"Nome:",Nome[y],"Senha:",Senha[y])