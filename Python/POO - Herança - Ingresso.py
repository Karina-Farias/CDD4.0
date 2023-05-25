class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R$ {self.valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional

ingresso1 = Ingresso(50.00)
ingresso1.imprimeValor()

vip1 = VIP(50, 50)
vip_valor = vip1.valorVIP()
print(f"Valor do ingresso VIP: R$ {vip_valor:.2f}")