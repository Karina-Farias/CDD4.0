Eleitores = int(input("Número de eleitores: "))
Branco = int(input("Número de votos brancos: "))
Nulo = int(input("Número de votos nulos: "))
Validos = int(input("Número de votos válidos: "))

PorcentagemBranco = (Branco/Eleitores)*100
print("A porcetagem de votos branco: ",PorcentagemBranco)

PorcentagemNulo = (Nulo*100)/Eleitores
print("A porcetagem de votos Nulo: ",PorcentagemNulo)

PorcentagemValidos = (Validos*100)/Eleitores
print("A porcetagem de votos Válidos: ",PorcentagemValidos)

