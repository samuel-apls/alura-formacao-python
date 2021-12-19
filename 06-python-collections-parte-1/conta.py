from abc import abstractmethod, ABCMeta
from operator import attrgetter
from functools import total_ordering

#class Conta(metaclass=ABCMeta):
@total_ordering
class Conta():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f'Código: {self._codigo} | Saldo: R${self._saldo}'

    @abstractmethod
    def passa_mes(self):
        pass
        #necessario parâmetro na classe para tornar obrigatória a implementação do método abstrato
    def __eq__(self, outro):
        return self._saldo == outro._saldo

    def __lt__ (self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

class ContaCorrente(Conta):
    
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

class ContaSalario(Conta):

    def __eq__(self, outro):
      return self._codigo == outro._codigo
    
    def __lt__ (self, outro):
        return self._codigo > outro._codigo

conta01 = ContaCorrente(1)
conta02 = ContaPoupanca(2)
conta03 = ContaInvestimento(3)
conta04 = ContaSalario(4)

contas = [conta01, conta02, conta03, conta04]

for conta in contas:
    conta.deposita(1000)
    conta.passa_mes()
    print(conta)

print(f'Conta04 é igual a Conta02? {conta04 == conta03}')
print(f'É um tipo de conta? {isinstance(conta04, Conta)}')
print(f'É um tipo de conta salário? {isinstance(conta04, ContaSalario)}')
print(f'É um tipo de conta corrente? {isinstance(conta04, ContaCorrente)}')
print(f'É um tipo de conta investimento? {isinstance(conta04, ContaInvestimento)}')
print('----------')
#Ordenação de objetos sem ordem natural (por parâmetro - saldo)
print('Ordenado por parâmetro - saldo:')
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)
print('----------')

#Ordenação de objetos sem ordem natural (por métodos mágicos - código)
print('Ordenado por "magic methods" - código:')
for conta in sorted(contas):
    print(conta)
print('----------')

#Ordem de ordenação
print(f'Conta 1 é igual a Conta 2? {contas[1] == contas[2]}')
print(f'Conta 2 é igual a Conta 3? {contas[2] == contas[3]}')
print('----------')
