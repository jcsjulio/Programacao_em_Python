# Solicitando os dados ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

# Utilizando match/case para selecionar a operação
match operacao:
    case '+':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        
    case '-':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        
    case '*':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        
    case '/':
        # Validação simples para evitar divisão por zero
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: Não é possível dividir por zero!")
            
    case _:
        # O caractere '_' funciona como o 'else', capturando qualquer opção inválida
        print("Operação inválida! Por favor, escolha +, -, * ou /.")
