ArrayImpar = []
contador = 0
impar = 0

while True:
    if contador % 2 != 0:
        ArrayImpar.append(contador)
        impar = impar + 1
    if impar == 10:
        break
    contador = contador + 1

print(ArrayImpar)