class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer...")

class Gato(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} foi miando...")

    def comer(self, comida):
        self.comida = comida
        print(f"{self.nome} está comendo {self.comida}")


class Cachorro(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} foi latir...")

    def comer(self, comida):
        self.comida = comida
        print(f"{self.nome} está comendo {self.comida}")

class Coelho(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} foi pular...")

class Vaca(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} foi mugir...")


gato1 = Gato("A gatinha Pite", "Amarelo")
cachorro1 = Cachorro("O cachorro Apolo","preto")
coelho1 = Coelho("O Coelho Bolinha","cinza")
vaca1 = Vaca("A vaca Bella","preta")


gato1.comer("ração")
cachorro1.comer("biscoito")
vaca1.comer()
coelho1.comer()