def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    """Exibe o menu de opções."""
    print("\nEscolha a opção desejada:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    print("0. Sair")

def main():
    print("Bem-vindo ao conversor de temperatura!")

    while True:
        menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
        elif escolha == "2":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"A temperatura em Celsius é: {celsius}°C")
        elif escolha == "0":
            print("Obrigado por usar o conversor de temperatura. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
