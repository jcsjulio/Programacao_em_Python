import math
from mod_continuar import deseja_continuar

def calcular_raio():
    print("--- Cálculo do Raio da Tubulação ---")
    while True:
        try:
            circunferencia = float(input("Digite o valor da circunferência (C): ").replace(',', '.'))
            if circunferencia <= 0:
                print("A circunferência precisa ser um número maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Insira um valor numérico válido.")

    # r = C / (2 * pi)
    raio = circunferencia / (2 * math.pi)
    
    print(f"\n💡 Resultado Técnico:")
    print(f"-> Para uma circunferência de {circunferencia:.2f}, o raio (r) é: {raio:.4f}\n")

loop_ativo = True
while loop_ativo:
    calcular_raio()
    loop_ativo = deseja_continuar("Deseja realizar um novo cálculo? (S/N): ")
