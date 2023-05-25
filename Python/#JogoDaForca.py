import random

# Lista de palavras
palavras = ["cachorro", "gato", "vaca", "peixe", "cobra"]

# Selecionar uma palavra aleatória da lista
palavra = random.choice(palavras)

# Inicializar variáveis
vidas = 6
letras_corretas = []
print("Tema: Animal")
# Loop principal do jogo
while True:
    # Mostrar a palavra atualizada com as letras corretas
    palavra_mostrada = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + " "
        else:
            palavra_mostrada += "_ "
    print(palavra_mostrada)

    # Solicitar uma letra do jogador
    letra = input("Digite uma letra: ")

    # Verificar se a letra está correta
    if letra in palavra:
        letras_corretas.append(letra)
        print("Letra correta!")
    else:
        vidas -= 1
        print("Letra incorreta! Você perdeu uma vida.")
        print("Vidas restantes:", vidas)

    # Verificar se o jogador ganhou ou perdeu
    if vidas == 0:
        print("Você perdeu! A palavra era:", palavra)
        break
    elif set(palavra) == set(letras_corretas):
        print("Parabéns! Você acertou a palavra é:", palavra,"!")
        break
