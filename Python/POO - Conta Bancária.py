class ContaBancaria:
    def __init__(self, numero_conta, nome_cliente, tipo_conta):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.status_conta = False
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.valor_limite = 0

    def depositar(self, valor):
        if self.status_conta:
            self.saldo += valor
            print(f"Depósito realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
        else:
            print("Não é possível depositar. A conta está desativada.")

    def sacar(self, valor):
        if self.status_conta:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
            elif self.saldo + self.valor_limite >= valor:
                valor_limite_utilizado = valor - self.saldo
                self.saldo = 0
                self.valor_limite -= valor_limite_utilizado
                print(f"Saque realizado utilizando o valor do limite! Saldo atual: R${self.saldo:.2f}")
            else:
                print(f"Saldo e valor do limite insuficientes para efetuar o saque. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Não é possível sacar. A conta está desativada.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def ativar_conta(self):
        if self.status_conta:
            print("A conta já está ativa.")
        else:
            self.status_conta = True
            print("A conta foi ativada.")

    def desativar_conta(self):
        if self.saldo == 0:
            self.status_conta = False
            print("A conta foi desativada.")
        else:
            print("Não é possível desativar a conta. O saldo não está zerado.")

    def ativar_limite(self,valor_liberado):
        if self.status_conta:
            self.valor_limite = valor_liberado
            print(f"Valor de Limite Liberado: R${self.valor_limite:.2f}")
        else:
            print("Não é possível liberar limite. A conta está desativada.")

    def desativar_limite(self):
        if self.status_conta:
            self.valor_limite = 0
            print(f"Valor do limite bloqueado!")
        else:
            print("Não é possível bloquear limite. A conta está desativada.")

# Exemplo de uso:
conta1 = ContaBancaria(123456, "João da Silva", "Corrente")

conta1.ativar_conta()
conta1.depositar(1000)
conta1.verificar_saldo()
conta1.sacar(500)
conta1.verificar_saldo()
conta1.desativar_conta()
conta1.verificar_saldo()
conta1.ativar_limite(50)
conta1.sacar(550)
conta1.verificar_saldo()
