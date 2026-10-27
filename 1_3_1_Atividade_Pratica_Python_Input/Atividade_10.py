# Recebendo a amperagem do chuveiro
amperagem = float(input("Digite a amperagem do chuveiro (A): "))

# Calculando o disjuntor com 10% de margem de sobra
disjuntor_necessario = amperagem * 1.10

# Exibindo o resultado usando vírgulas para separar os textos e números
print("O disjuntor adequado deve ser de no mínimo:", round(disjuntor_necessario, 2), "A")
