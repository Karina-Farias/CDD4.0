class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, andando=False, falando=False):
        self.nome =  nome
        self.peso =  peso
        self.idade = idade
        self.comendo = comendo
        self.andando = andando
        self.falando = falando

    def comer(self, comida):
        self.comida = comida
        if self.comendo == False:
            print(f'{self.nome} está comendo {self.comida}')
            self.comendo = True
        else:
            print(f'{self.nome} já está comendo!')

    def paradecomer(self):
        if self.comendo ==True:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo')

    def andar(self):
        if self.andando == False:
            print(f'{self.nome} começou a andar!')
            self.comendo = True
        else:
            print(f'{self.nome} já está andando!')

    def paradeandar(self):
        if self.andando ==True:
            print(f'{self.nome} parou de andar')
            self.andando = False
        else:
            print(f'{self.nome} não está andando!')

    def falar(self):
        if self.falando == False:
            if self.comendo == False:
                print(f'{self.nome} não está comendo nem falando, então ele pode falar!')
                self.falando = True
        else:
            print(f'{self.nome} já está falando!')

    def paradefalar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar!')
        elif self.comendo == True:
            print(f'{self.nome} está comendo por isso não pode falar!')
        else:
            print(f'{self.nome} não está falando!')

p1 = Pessoa("João", 80, 19)
p2 = Pessoa("Maria",56 , 22, comendo=True)

p1.comer("pipoca")
p1.falar()
p1.paradefalar()
p1.andar()
p1.paradeandar()
#p1.comer("Pão")



#print(p1.nome)
#print(vars(p1))
#print(p2.nome)
#print(vars(p2))