valor1 = float(input("Valor 1:"))
while valor1 <= 0:
    print("Digite um valor maior que zero:")
    valor1 = float(input())

valor2 = float(input("Valor 2:"))
while valor2 <= 0:
    print("Digite um valor maior que zero:")
    valor2 = float(input())

divisao = valor1 / valor2
print("A divisão do", valor1, "e do", valor2, "é", divisao)
