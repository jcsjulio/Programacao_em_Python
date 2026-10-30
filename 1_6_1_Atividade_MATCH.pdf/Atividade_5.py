print("--- SISTEMA DE SUPORTE AO CLIENTE ---")
print("1 – Computador não liga.")
print("2 – Computador lento.")
print("3 – Problema de internet.")
print("4 – Problema de impressão.")

opcao = int(input("Selecione o número do problema relatado (1-4): "))

# Utilizando match/case para orientar o cliente de acordo com o problema
match opcao:
    case 1:
        print("\nOrientação: Verifique se o cabo de força está conectado à tomada e se o filtro de linha está ligado.")
    case 2:
        print("\nOrientação: Feche programas em segundo plano, limpe arquivos temporários ou reinicie o sistema.")
    case 3:
        print("\nOrientação: Desconecte o modem/roteador da tomada por 30 segundos, ligue-o novamente e teste a conexão.")
    case 4:
        print("\nOrientação: Verifique se há papel na bandeja, se os cartuchos/toners estão carregados e se o cabo USB está firme.")
    case _:
        print("\nOpção inválida! Por favor, selecione um problema de 1 a 4.")
