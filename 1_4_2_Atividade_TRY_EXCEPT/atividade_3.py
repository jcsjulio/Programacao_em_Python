try:
    preco = float(input("Digite o preço original do produto (R$): "))
    desconto_perc = float(input("Digite o percentual de desconto (%): "))
    
    # Calcula o valor do desconto e o preço final
    valor_desconto = preco * (desconto_perc / 100)
    preco_final = preco - valor_desconto
    
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
except ValueError:
    print("Erro: Os valores digitados para preço ou desconto são inválidos.")
