from typing import FrozenSet


usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

#Cópia raza (shalow copy) de uma lista
assistiram = []
assistiram = usuarios_data_science.copy()
print(f'Cópia da lista "usuarios_data_science: "{assistiram}')
print('----------')

#Transformação de uma lista em conjunto
#Conjuntos não possuem elementos repetidos, nem índice e nem ordem
#Usa-se chaves para criar um conjunto diretamente
assistiram = set(assistiram)
print(f'Conjunto de "assistiram": {assistiram}')
print('----------')

#União de conjuntos
#Necessário ser tipo set
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
assistiram = usuarios_data_science | usuarios_machine_learning
print(f'União de conjuntos: {assistiram}')
print('----------')

#Intersecção de conjuntos
#Necessário ser tipo set
assistiram = usuarios_data_science & usuarios_machine_learning
print(f'Intersecção de conjuntos: {assistiram}')
print('----------')

#Subtração de conjuntos
#Necessário ser tipo set
assistiram = usuarios_data_science - usuarios_machine_learning
print(f'Subtração de conjuntos: {assistiram}')
print('----------')

#OU exclusivo de conjuntos
#Necessário ser tipo set
assistiram = usuarios_data_science ^ usuarios_machine_learning
print(f'OU exclusivo de conjuntos: {assistiram}')
print('----------')

#Operações
#Adicionar em conjunto, pois é mutável
usuarios = {1,5,76,34,52,13,17}
usuarios.add(765)
print(f'Conjunto de "usuarios": {usuarios}')
print('----------')

#Congelar cnjunto (torna imutável)
usuarios = frozenset(usuarios)
print(f'Conjunto de "usuarios": {usuarios}')
print('----------')

#Conjunto com String
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(f'Texto em conjunto: {set(meu_texto.split())}')
print('----------')
