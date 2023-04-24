NotaAlunos= []
soma = 0
contador = 0

for i in range(5):
    NotaAlunos.append(float(input("Digite uma nota:")))

for x in range(5):
    soma += NotaAlunos[x]

media = soma/5

for y in range(5):
    if NotaAlunos[y] >= media:
        contador = contador + 1
print(contador,"Alunos ficaram com notas igual ou maior que a média.")
