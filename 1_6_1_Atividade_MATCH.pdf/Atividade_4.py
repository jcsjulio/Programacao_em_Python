# Solicitando o valor do produto e a categoria
valor_venda = float(input("Digite o valor total da venda: R$ "))

print("\n--- CATEGORIAS ---")
print("1 – Informática (10% de desconto)")
print("2 – Eletrônicos (5% de desconto)")
print("3 – Acessórios (2% de desconto)")
categoria = int(input("Escolha a categoria do produto (1-3): "))

# Utilizando match/case para definir o percentual de desconto
match categoria:
    case 1:
        desconto = 0.10  # 10%
    case 2:
        desconto = 0.05  # 5%
    case 3:
        desconto = 0.02  # 2%
    case _:
        desconto = 0.00
        print("Categoria inválida! Nenhum desconto será aplicado.")

# Calculando os valores finais
valor_desconto = valor_venda * desconto
valor_final = valor_venda - valor_desconto

# Exibindo os resultados formatados
print(f"\nDesconto aplicado: R$ {valor_desconto:,.2f}")
print(f"Valor final a pagar: R$ {valor_final:,.2f}")
