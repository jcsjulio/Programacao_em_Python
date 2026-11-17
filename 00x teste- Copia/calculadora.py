from utils import exibir_banner, ler_int, ler_float, pausar

def executar_calculadora():
    while True:
        exibir_banner("CALCULADORA")
        print("--- CALCULADORA DE PROCESSAMENTO ---\n")
        print(" [1] Adição")
        print(" [2] Subtração")
        print(" [3] Divisão")
        print(" [4] Somatória (vários números)")
        print(" [5] Porcentagem")
        print(" [0] Voltar ao Menu Principal")

        opcao = ler_int("\nEscolha uma operação: ", minimo=0, maximo=5)

        if opcao == 0:
            break

        elif opcao == 1:
            print("\n--- ADIÇÃO ---")
            n1 = ler_float("Primeiro número: ", permitir_zero=True)
            n2 = ler_float("Segundo número: ", permitir_zero=True)
            print(f"\nResultado: {n1} + {n2} = {n1 + n2}")

        elif opcao == 2:
            print("\n--- SUBTRAÇÃO ---")
            n1 = ler_float("Primeiro número: ", permitir_zero=True)
            n2 = ler_float("Segundo número: ", permitir_zero=True)
            print(f"\nResultado: {n1} - {n2} = {n1 - n2}")

        elif opcao == 3:
            print("\n--- DIVISÃO ---")
            n1 = ler_float("Dividendo: ", permitir_zero=True)
            while True:
                n2 = ler_float("Divisor: ", permitir_zero=True)
                try:
                    resultado = n1 / n2
                    print(f"\nResultado: {n1} / {n2} = {resultado:.4f}")
                    break
                except ZeroDivisionError:
                    print("Erro: Não é possível dividir por zero. Tente novamente.\n")

        elif opcao == 4:
            print("\n--- SOMATÓRIA ---")
            qtd = ler_int("Quantos números deseja somar? ", minimo=2)
            soma = 0.0
            for i in range(1, qtd + 1):
                num = ler_float(f"Digite o {i}º número: ", permitir_zero=True)
                soma += num
            print(f"\nResultado da Somatória: {soma}")

        elif opcao == 5:
            print("\n--- PORCENTAGEM ---")
            valor = ler_float("Valor base: ", permitir_zero=True)
            percentual = ler_float("Porcentagem (%): ", permitir_zero=True)
            resultado = (valor * percentual) / 100
            print(f"\nResultado: {percentual}% de {valor} = {resultado}")

        pausar()
