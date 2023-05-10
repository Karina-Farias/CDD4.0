TipoCombustivel = input("Digite o Tipo do Combustivel: G - Gasolina / E - Etanol:")
Qlitros = float(input("Litros comprado:"))

if TipoCombustivel == "e":
    ValorTotal = Qlitros * 4.9
    print("Valor Pago:", ValorTotal)
elif TipoCombustivel == "g":
    ValorTotal = Qlitros * 5.8
    print("Valor Pago:", ValorTotal)
else:
    print("Tipo do Combustivel inválido!")
