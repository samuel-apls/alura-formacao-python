idades = [15, 87, 32, 65, 56, 32, 49, 37]

#Imprimir as posições com seus valores
for posicao in list(enumerate(idades)):
    print(posicao)
print('----------')

#... Utilizando o iterador LIST para imprimir
print(list(enumerate(idades)))
print('----------')

#... Desempacotando a tupla
for posicao, valor in enumerate(idades):
    print(f'[{posicao}]: {valor}')
print('----------')

#Ordenar idades
print(f'Lista ordenada: {sorted(idades)}')
print('----------')

#Inverter ordem
#print(f'Lista ordenada: {list(reversed(idades))}')
print(f'Lista ordenada: {sorted(idades, reverse=True)}')
print('----------')

#Ordenar idades na referência
idades.sort()
print(f'Lista ordenada na referência: {idades}')
print('----------')
