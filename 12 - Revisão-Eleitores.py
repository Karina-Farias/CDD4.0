Eleitores = int(input("Número de eleitores: "))
Brancos = int(input("Número de votos brancos: "))
Nulos = int(input("Número de votos nulos: "))
Validos = int(input("Número de votos válidos: "))

PorcentagemBrancos = (Brancos/Eleitores)*100
PorcentagemNulos = (Nulos*100)/Eleitores
PorcentagemValidos = (Validos*100)/Eleitores

if PorcentagemBrancos + PorcentagemNulos + PorcentagemValidos > 100:
    print("Inválido! Houve fraude")

elif PorcentagemBrancos + PorcentagemNulos + PorcentagemValidos < 100:
    print("Inválido! Houve fraude")

else:
    print("A porcetagem de votos Brancos: ",PorcentagemBrancos)
    print("A porcetagem de votos Nulos: ",PorcentagemNulos)
    print("A porcetagem de votos Válidos: ",PorcentagemValidos)