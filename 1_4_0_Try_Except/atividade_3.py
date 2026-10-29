try:
    numerador = float(input("Digite o numerador (dividendo): "))
    denominador = float(input("Digite o denominador (divisor): "))
    
    resultado = numerador / denominador
    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    print("Erro: Por favor, digite apenas valores numéricos.")

except ZeroDivisionError:
    print("Erro: Não é possível realizar uma divisão por zero.")
