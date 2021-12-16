#Criar uma classe e métodos
class Conta_Corrente():
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'Códido: {self.codigo} | Saldo: {self.saldo}'

conta_samuel = Conta_Corrente(1)
conta_manu = Conta_Corrente(2)
conta_saulo = Conta_Corrente(3)
conta_samuel.deposita(1)
conta_manu.deposita(2)
conta_saulo.deposita(3)

#Criar uma lista de referência para objetos
contas = [conta_samuel, conta_manu, conta_saulo]
for conta in contas:
    print(f'Lista: {conta}')

#Fazer tupla de listas
tupla = ([conta_samuel, 35], [conta_manu, 37], [conta_saulo, 2])
for elemento in tupla:
    print(f'Tupla: {elemento}')

#Fazer uma lista de tuplas
lista = [(conta_samuel, 35), (conta_manu, 37), (conta_saulo, 2)]
for elemento in lista:
    print(f'Lista: {elemento}')
