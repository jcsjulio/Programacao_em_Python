# Requisito: Utilize INPUT para receber o número.
numero = int(input("Digite um número inteiro: "))

# Variável de controle para o multiplicador (iniciando em 1)
multiplicador = 1

print(f"\nTabuada do {numero}:")

# Requisito: Utilize WHILE para controlar a repetição.
while multiplicador <= 10:
    # Requisito: Multiplique o número informado pelos valores de 1 até 10.
    resultado = numero * multiplicador
    
    # Requisito: Apresente os resultados na tela.
    print(f"{numero} x {multiplicador} = {resultado}")
    
    # Incrementa o multiplicador para passar para o próximo número
    multiplicador += 1
