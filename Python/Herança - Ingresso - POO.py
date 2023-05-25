class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R$ {self.valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self, adicional):
        self.adicional = adicional
        self.valor = self.valor + self.adicional
        print(f"Valor do ingresso VIP: R$ {self.valor:.2f}")

ingresso1 = Ingresso(50.00)
vip1 = VIP(15)

ingresso1.imprimeValor()
vip1.imprimeValor(50)




