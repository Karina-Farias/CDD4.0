VetorA = []
VetorB = []
Soma = []

TamanhoLista = int(input("Digite o tamanho da lista:"))

for x in range(TamanhoLista):
    VetorA.append(int(input("Digite um valor do Vetor A:")))
    VetorB.append(int(input("Digite um valor do Vetor B:")))

for y in range(TamanhoLista):
    Soma.append(VetorA[y]+VetorB[y])

print(VetorA)
print(VetorB)
print(Soma)


