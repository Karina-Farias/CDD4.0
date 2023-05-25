class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

class Gato(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"{self.nome} foi miando...")


class Cachorro(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} foi latir...")

class Coelho(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} foi pular...")

class Vaca(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} foi mugir...")


gato1 = Gato("A gatinha Pite", "Amarelo")
cachorro1 = Cachorro("O cachorro Apolo","preto")
coelho1 = Coelho("O Coelho Bolinha","cinza")
vaca1 = Vaca("A vaca Bella","preta")

gato1.miar()
cachorro1.latir()
coelho1.pular()
vaca1.mugir()
