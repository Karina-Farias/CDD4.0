Vetor = []
contador = 0

for x in range(10):
    Vetor.append(int(input("Digite um valor:")))

n = int(input("Digite um número para pesquisar:"))

for y in range(10):
    if n == Vetor[y]:
        contador = contador + 1

print("O número",n,"apareceu",contador,"vezes.")
