def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    conta = conta['saldo']
    print(f'O saldo da conta é {conta}')

conta = cria_conta(123, "Nico", 55.0, 1000.0)
deposita(conta, 300.0)
extrato(conta)
saca(conta, 100.0)
extrato(conta)