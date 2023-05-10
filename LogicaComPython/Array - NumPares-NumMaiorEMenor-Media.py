Vetor = []
Soma = 0

for x in range(10):
    Vetor.append(int(input("Digite um valor:")))
    Soma = Soma+Vetor[x]

#Resolução do Item 1:
for a in range(10):
    if Vetor[a] % 2 == 0:
        print(Vetor[a],"",end="")

print()

#Resolução do Item 2:
Maior = Vetor[0]
Menor = Vetor[0]

for b in range(10):
    if Vetor[b] > Maior:
        Maior = Vetor[b]


    if Vetor[b] > Menor:
        Menor = Vetor[b]

print("O Maior Número é:",Maior)
print("O Menor Número é:", Menor)

print()

#Resolução do Item 3:
Media = Soma/10
Contador = 0

for c in range(10):
    if Vetor[c] > Media:
        Contador = Contador + 1
print("A quantidades de números maiores que a média é:",Contador)


