# Solicitando o número do dia ao usuário
dia = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

# Utilizando match/case para mapear o dia correspondente
match dia:
    case 1:
        print("1 - Domingo")
    case 2:
        print("2 - Segunda-feira")
    case 3:
        print("3 - Terça-feira")
    case 4:
        print("4 - Quarta-feira")
    case 5:
        print("5 - Quinta-feira")
    case 6:
        print("6 - Sexta-feira")
    case 7:
        print("7 - Sábado")
    case _:
        # Captura qualquer número fora da faixa de 1 a 7
        print("Número inválido! Por favor, digite um valor entre 1 e 7.")
