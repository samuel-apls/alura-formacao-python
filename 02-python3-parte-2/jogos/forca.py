from random import randrange


def jogar():
    exibe_abertura()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = acertos(palavra_secreta)

    chute = pede_chute()

    processa_jogada(palavra_secreta, chute, letras_acertadas)


def exibe_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def gera_palavra_secreta():
    palavras = []
    with open('palavras.txt', encoding='utf8') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())
    return palavras[randrange(0, len(palavras))]


def acertos(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def pede_chute():
    return input('Qual letra? ').strip().upper()


def registra_acerto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            print(f'A letra {letra} foi encontrada na posição {index}')
            letras_acertadas[index] = letra
        index += 1


def registra_erro(palavra_secreta, tentativa):
    erros = len(palavra_secreta) - tentativa + 1
    print(f'Que pena, você errou! Você usou {erros}/{len(palavra_secreta)} chances')
    desenha_forca(erros)
    return tentativa - 1


def processa_jogada(palavra_secreta, chute, letras_acertadas):
    tentativa = len(palavra_secreta)
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        if chute in palavra_secreta:
            registra_acerto(chute, palavra_secreta, letras_acertadas)
            print(letras_acertadas)
            # chute = pede_chute()
        else:
            tentativa = registra_erro(palavra_secreta, tentativa)

        enforcou = tentativa == 0
        acertou = "_" not in letras_acertadas

        if "_" not in letras_acertadas:
            exibe_vencedor()
        elif tentativa > 0:
            chute = pede_chute()
        else:
            exibe_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros >= 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def exibe_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def exibe_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
