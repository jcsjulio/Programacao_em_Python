# Solicita a nota ao usuário (usando float para permitir casas decimais)
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Classificação conforme as regras
if nota < 0 or nota > 10:
    print("Nota inválida.")
elif nota <= 4.9:
    print("Reprovado.")
elif nota <= 6.9:
    print("Recuperação.")
else:
    print("Aprovado.")
