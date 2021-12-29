#Criando um dicionário
aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

dicionario1 = dict(chave1 = 1, chave2 = 2)

dicionario2 = dict([('chave1', 1), ('chave2', 2)])

#Buscar valor direto pela chave
print(f'Valor direto pela chave "Guilherme": {aparicoes["Guilherme"]}')
print('----------')

#Buscar valor direto por método
print(f'Valor por método get(): {aparicoes.get("Guilherme", 0)}')
print('----------')

#Manipulando dicionario
aparicoes['Temporario1'] = 99
print(f'Adicionando chave "Temporario1": {aparicoes.get("Temporario1")}')
print('----------')

del aparicoes['Temporario1']
print(f'Removendo chave "Temporario1": {aparicoes}')
print('----------')

#Iteração no dicionaário
print(f'Percorrendo o dicionário pela chave "Guilherme": {"Guilherme" in aparicoes}')
print('----------')

print('Percorrendo chaves:')
for chave in aparicoes:
    print(chave)
print('----------')

print('Percorrendo chaves e valoress:')
for chave in aparicoes.items():
    print(chave)
print('----------')

print('Percorrendo chaves e valores desempacotados:')
for chave, valor in aparicoes.items():
    print(chave, ":", valor)
print('----------')

#Contagem de strings
from collections import defaultdict
from typing import Counter
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

#Método de contagem iterando
aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)
print('----------')

#método de contagem por método
aparicoes = Counter(meu_texto.split())
print(aparicoes)
print('----------')
