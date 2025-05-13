def mostrar_forca(erros):
    boneco = [
        '''
           ------
           |    |
           |
           |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        '''
    ]
    print(boneco[erros])


def jogar_forca():
    palavra_secreta = "python"
    letras_descobertas = ["_" for _ in palavra_secreta]
    tentativas = 0
    letras_erradas = []

    while tentativas < 6 and "_" in letras_descobertas:
        mostrar_forca(tentativas)
        print("Palavra: ", " ".join(letras_descobertas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            print("Letra errada!")
            tentativas += 1
            letras_erradas.append(letra)

    mostrar_forca(tentativas)
    if "_" not in letras_descobertas:
        print("Parabéns! Você acertou a palavra:", palavra_secreta)
    else:
        print("Você perdeu! A palavra era:", palavra_secreta)


jogar_forca()