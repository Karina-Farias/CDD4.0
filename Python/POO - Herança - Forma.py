class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = self.base * self.altura
        print("Retângulo:")
        print(f"Área: {retangulo.area}")

    def calculaPerimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        print(f"Perímetro: {retangulo.perimetro}")

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = (self.base * self.altura) / 2
        print("\nTriângulo:")
        print(f"Área: {triangulo.area}")

    def calculaPerimetro(self):
        # Para fins de exemplo, considerando um triângulo retângulo
        hipotenusa = ((self.base ** 2) + (self.altura ** 2)) ** 0.5
        self.perimetro = self.base + self.altura + hipotenusa
        print(f"Perímetro: {triangulo.perimetro}")

retangulo = Retangulo(5, 3)
retangulo.calculaArea()
retangulo.calculaPerimetro()

triangulo = Triangulo(4, 6)
triangulo.calculaArea()
triangulo.calculaPerimetro()

print("\nVerificando as instâncias:")
print(f"retangulo é instância de Forma: {isinstance(retangulo, Forma)}")
print(f"triangulo é instância de Forma: {isinstance(triangulo, Forma)}")
