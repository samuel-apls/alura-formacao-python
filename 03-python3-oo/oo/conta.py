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
    
    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Impossível sacar R$ {valor} para o Sr. {self.titular}, pois está acima do limite")

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

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

""" conta = Conta(123, "Nico", 100, 1000)
conta2 = Conta(456, "Marcos", 100, 1000)
conta.saca(1100)
conta2.saca(1100)
conta.saldo
conta2.saldo
print(Conta.codigo_banco())
print(Conta.codigos_bancos()) """
