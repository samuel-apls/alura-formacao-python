idades = [1, 2, 3, 4, 5]
print(f'Lista {idades}')

print(f'Tipo: {type(idades)}')
print(f'Tamanho: {len(idades)}')
print(f'Valor na posição 0: {idades[0]}')

idades[0] = 0
print(f'Altera valor na posição 0: {idades[0]}')
idades[0] = 1

idades.append(6)
print(f'Adiciona valor na última posição: {idades}')

idades.insert(len(idades) + 1, 7)
print(f'Insere valor na posição: {idades}')

i = 0
for elemento in idades:
    print(f'Percorrento elemento [{i}]: {elemento}')
    i += 1

idades.remove(6)
idades.remove(7)
print(f'Remover primeira ocorrência: {idades}')

idades.clear()
print(f'Limpa toda a lista: {idades}')

idades = [1, 2, 3, 4, 5]
print(f'Valida se valor existe na lista: {1 in idades}')

idades2 = [elemento + 1 for elemento in idades]
print(f'List Comprehension: {idades2}')

idades2 = [elemento for elemento in idades if elemento %2 == 0]
print(f'List Comprehension com critério: {idades2}')

#Lista com valor padrão
def cria_lista(lista = None):
    if lista == None:
        lista = list()

idades = [1, 2, 3, 4, 5]
idades.append([6, 7])
print(f'Imprime tupla: {idades}')

idades.extend([6, 7])
idades.remove([6, 7])
print(f'Imprime tupla expandida: {idades}')
