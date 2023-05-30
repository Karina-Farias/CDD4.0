class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print("O Atleta se aposentou.")

    def aquecer(self):
        self.aquecendo = True
        print("O atleta está se aquecendo.")


class Corredor(Atleta):
    def correr(self):
        if self.aposentado == False:
            self.correr = True
            if self.aquecendo == True:
                print("O corredor está correndo.")
            else:
                print("O corredor não pode correr, pois ele não se aqueceu ainda!")
        else:
            print("O corredor não pode correr, pois ele está aposentado!")

    def parar_correr(self):
        if self.correr == True:
            print("O corredor parou de correr.")
        else:
            print("O corredor ainda não começou a correr, por isso, ele não pode parar!")


class Nadador(Atleta):
    def nadar(self):
        if self.aposentado == False:
            self.nadar = True
            if self.aquecendo == True:
                print("O nadador está nadando.")
            else:
                print("O nadador não pode nadar, pois ele não se aqueceu ainda!")
        else:
            print("O nadador não pode nadar, pois ele está aposentado!")

    def parar_nadar(self):
        if self.nadar == True:
            print("O nadador parou de nadar.")
        else:
            print("O nadador ainda não começou a nadar, por isso, ele não pode parar!")


class Ciclista(Atleta):
    def pedalar(self):
        if self.aposentado == False:
            self.pedalar = True
            if self.aquecendo == True:
                print("O ciclista está pedalando.")
            else:
                print("O ciclista não pode pedalar, pois ele não se aqueceu ainda!")
        else:
            print("O cilista não pode peladar, pois ele está aposentado!")

    def parar_pedalar(self):
        if self.pedalar == True:
            print("O ciclista parou de pedalar.")
        else:
            print("O ciclista ainda não começou a pedalar, por isso, ele não pode parar!")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)


# Exemplo de uso das classes
triatleta1 = TriAtleta(False, 70)

triatleta1.aquecer()  # Saída: O atleta está se aquecendo.
triatleta1.correr()  # Saída: O corredor está correndo.
triatleta1.nadar()  # Saída: O nadador está nadando.
triatleta1.pedalar()  # Saída: O ciclista está pedalando.

triatleta1.parar_correr()  # Saída: O corredor parou de correr.
triatleta1.parar_nadar()  # Saída: O nadador parou de nadar.
triatleta1.parar_pedalar()  # Saída: O ciclista parou de pedalar.

triatleta1.aposentar()
