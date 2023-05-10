Texto = "O rato roeu a roupa do rei de Roma"
def vogais(Texto2):
    contador = 0
    for x in Texto2:
        if x in "aeiouAEIOU":
            contador = contador + 1
    print(f"O número de vogais é {contador}")

vogais(Texto)
