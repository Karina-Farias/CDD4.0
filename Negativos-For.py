negativos = 0 # contador dos negativos

for i in range(10): #Loop para ler 10 Valores
    n = float(input("Digite um número:"))
    if n < 0:
        negativos = negativos + 1 # Se o numero for negativo, incrementa na variavel negativos

print("Foram digitados", negativos, "números negativos.")