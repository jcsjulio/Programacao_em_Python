# Solicita a idade ao usuário
idade = int(input("Digite a idade: "))

# Classificação conforme as regras
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
else:
    print("Adulto.")
