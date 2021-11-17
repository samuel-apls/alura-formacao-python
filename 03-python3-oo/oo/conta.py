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
    
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.extrato()
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

""" conta = Conta(123, "Nico", 100, 1000.0)
conta2 = Conta(456, "Marcos", 100, 1000.0)
conta.transfere(100, conta2)
conta.saldo
conta2.saldo """
