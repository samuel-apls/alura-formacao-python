class Conta:

    def __init__(self,numero, titular, saldo, limite):
        #print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"O saldo de {self.saldo} do titular {self.titular }")
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor

""" conta = Conta(123, "Nico", 1, 1000.0)
conta.deposita(300.0)
conta.extrato()
conta.saca(100.0)
conta.extrato() """
