VetorA = []
VetorM = []

for x in range(10):
    VetorA.append(int(input("Digite um valor:")))

x = int(input("Digite o multiplicador:"))

for y in range(10):
    VetorM.append(VetorA[y]*x)

print(VetorA)
print(x)
print(VetorM)
