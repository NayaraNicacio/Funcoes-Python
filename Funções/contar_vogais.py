def contar_vogais(frase):
    """Conta o número de vogais em uma string."""
    vogais = "aeiouAEIOU"
    total_vogais = 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
    return total_vogais

def main():
    frase = input("Digite uma frase para contar as vogais: ")
    total = contar_vogais(frase)
    print("O total de vogais na frase é:", total)

if __name__ == "__main__":
    main()
