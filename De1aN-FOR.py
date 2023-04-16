#range(inicio, fim, passo) - range(start, stop, step)
n = int(input("Digite um número:"))

if n > 0:
    for i in range(1,n+1):
        print(i)
else:
    n = int(input("Número precisa ser maior que zero! Informe outro número:"))
    if n > 0:
        for i in range(1,n+1):
            print(i)
