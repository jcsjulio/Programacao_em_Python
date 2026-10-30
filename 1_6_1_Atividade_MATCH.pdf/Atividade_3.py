# Configurando o saldo inicial exigido pelo exercício
saldo = 1000.00

# Loop para manter o menu ativo até que o usuário escolha sair
while True:
    print("\n--- MENU BANCÁRIO ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    
    opcao = int(input("Escolha uma opção (1-4): "))
    
    match opcao:
        case 1:
            print(f"Seu saldo atual é: R$ {saldo:,.2f}")
            
        case 2:
            valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
            if valor_deposito > 0:
                saldo += valor_deposito
                print(f"Depósito de R$ {valor_deposito:,.2f} realizado com sucesso!")
            else:
                print("Valor de depósito inválido.")
                
        case 3:
            valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            elif valor_saque <= 0:
                print("Valor de saque inválido.")
            else:
                saldo -= valor_saque
                print(f"Saque de R$ {valor_saque:,.2f} realizado com sucesso!")
                
        case 4:
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break  # Encerra o loop e finaliza o programa
            
        case _:
            print("Opção inválida! Por favor, selecione uma opção de 1 a 4.")
