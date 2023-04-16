intervalo = 0
fora = 0

for i in range(10): #Loop para ler 10 Valores
    n = float(input("Digite um número:"))
    if n >= 10 and n <= 20:
        intervalo = intervalo + 1

    else:
        fora = fora + 1

print("Foram digitados",intervalo, "números no intervalo de 10 e 20.")
print("Foram digitados",fora, "números fora do intervalo de 10 e 20.")