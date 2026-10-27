

# Recebendo a potência e a voltagem
potencia = float(input("Digite a potência do chuveiro (em Watts/W): "))
voltagem = float(input("Digite a tensão/voltagem da tomada (em Volts/V): "))

# Calculando a amperagem (Corrente = Potência / Voltagem)
amperagem = potencia / voltagem

# Calculando o disjuntor com 10% de margem de sobra
disjuntor_necessario = amperagem * 1.10

# Exibindo o resultado separado por vírgulas
print("A amperagem do chuveiro é:", round(amperagem, 2), "A")
print("O disjuntor adequado deve ser de no mínimo:", round(disjuntor_necessario, 2), "A")
    
