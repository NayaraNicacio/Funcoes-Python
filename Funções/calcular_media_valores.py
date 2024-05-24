def calcular_media():
    valores = []
    continuar = True
    
    while continuar:
        entrada = input("Digite um número ou 'ok' para calcular a média: ")
        if entrada.lower() == "ok":
            if len(valores) == 0:
                print("Nenhum valor foi inserido para calcular a média.")
                
            else:
                media = sum(valores) / len(valores)
                print("A média dos valores inseridos é:", media)
                return entrada, media
        else:
            try:
                valor = float(entrada)
                valores.append(valor)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

# Teste da função
calcular_media()
