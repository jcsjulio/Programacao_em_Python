from mod_continuar import deseja_continuar

def menu_calculadora():
    print("--- Calculadora Avançada ---")
    print("[1] Soma (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")
    
    while True:
        opcao = input("Selecione a operação (1-4): ").strip()
        if opcao in ['1', '2', '3', '4']:
            return opcao
        print("Opção inválida! Escolha um número entre 1 e 4.")

def executar_operacao():
    operacao = menu_calculadora()
    
    while True:
        try:
            num1 = float(input("Digite o primeiro número: ").replace(',', '.'))
            num2 = float(input("Digite o segundo número: ").replace(',', '.'))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    print("\n--- Resultado ---")
    if operacao == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == '4':
        if num2 == 0:
            print("Erro crítico: Não é possível realizar uma divisão por zero!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    print("-" * 17 + "\n")

if __name__ == "__main__":
    loop_ativo = True
    while loop_ativo:
        executar_operacao()
        loop_ativo = deseja_continuar("Deseja realizar um novo cálculo matemático? (S/N): ")
