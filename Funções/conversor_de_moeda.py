carteira= float (input ("Digite a Quantidade de Dinheiro de sua carteira: $\n"))
cambio =  {
  "Dólar_Americano":4.91,
  "Peso_Argentino": 0.02,
  "Dólar_Australiano": 3.18,
  "Dólar_Canadense": 3.64,
  "Franco_Suiço": 0.42,
  "Euro": 5.36,
  "Libra_esterlina": 6.21
}
if carteira > 0:
    for key, value in cambio.items():
        if value > -1:
            print(f"Com o valor de $: {carteira} você compra $: {carteira / value:,.2f} {key}")
else:
    print("Digite um valor maior que 0")