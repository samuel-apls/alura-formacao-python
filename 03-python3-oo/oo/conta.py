class Conta:

    def __init__(self,numero, titular, saldo, limite):
        #print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo é de R$ {self.__saldo} do titular {self.__titular }")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

""" conta = Conta(123, "Nico", 100, 1000.0)
conta2 = Conta(456, "Marcos", 100, 1000.0)
conta.transfere(100, conta2)
conta.extrato()
conta2.extrato() """
