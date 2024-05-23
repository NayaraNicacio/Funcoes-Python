import random

def escolher_palavra():
    """Função para escolher uma palavra aleatória da lista predefinida."""
    palavras = ["python", "programacao", "computador", "inteligencia", "desenvolvimento", "openai", "jogo", "forca"]
    return random.choice(palavras)

def inicializar_palavra_secreta(palavra):
    """Função para inicializar a palavra secreta com espaços em branco."""
    return ["_"] * len(palavra)

def mostrar_palavra_secreta(palavra_secreta):
    """Função para mostrar a palavra secreta."""
    print("Palavra secreta:", " ".join(palavra_secreta))

def jogar_forca():
    """Função principal para jogar o jogo da forca."""
    palavra = escolher_palavra()
    palavra_secreta = inicializar_palavra_secreta(palavra)
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    mostrar_palavra_secreta(palavra_secreta)

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            print("Letra correta!")
            # Revela a letra nas posições correspondentes na palavra secreta
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra
            mostrar_palavra_secreta(palavra_secreta)
        else:
            print("Letra errada!")
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letras erradas:", " ".join(letras_erradas))
            print("Tentativas restantes:", tentativas)
        
        if "_" not in palavra_secreta:
            print("Parabéns! Você ganhou!")
            break
        elif tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra)
            break

if __name__ == "__main__":
    jogar_forca()
