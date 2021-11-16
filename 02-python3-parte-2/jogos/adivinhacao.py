from random import randrange


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = randrange(1, 101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(rodada, tentativas + 1):
        print(f'--Tentativa {rodada} de {tentativas} --')
        chute = int(input('Digite o seu número: '))
        print(f'Você digitou {chute}')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'Parabéns! Você acertou e fez {pontos} pontos.\n')
            break
        else:
            if maior:
                print('O seu chute foi maior do que o número secreto!\n')
            elif menor:
                print('O seu chute foi menor que o número secreto\n')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print('Fim do jogo')

if(__name__ == "__main__"):
    jogar()
