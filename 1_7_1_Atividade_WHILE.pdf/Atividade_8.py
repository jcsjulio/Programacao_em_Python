# Definindo as configurações do jogo
NUMERO_SECRETO = 25
tentativas = 0

print("--- JOGO DE ADIVINHAÇÃO ---")
print("Tente adivinhar o número secreto!")

# Requisito: Utilize WHILE para repetir as tentativas.
while True:
    # Requisito: Utilize INPUT para receber os palpites.
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1  # Incrementa o número de tentativas feitas
    
    if palpite == NUMERO_SECRETO:
        # Requisito: Quando acertar, exiba: "Parabéns! Você acertou!".
        print("\nParabéns! Você acertou!")
        break  # Encerra o loop pois o jogo acabou
        
    # Requisito: Se o número informado for maior que 25, exiba: "O número secreto é menor!".
    elif palpite > NUMERO_SECRETO:
        print("O número secreto é menor!")
        
    # Requisito: Se o número informado for menor que 25, exiba: "O número secreto é maior!".
    else:
        print("O número secreto é maior!")

# Requisito: Informe quantas tentativas foram necessárias.
print(f"Você precisou de {tentativas} tentativa(s) para vencer.")
