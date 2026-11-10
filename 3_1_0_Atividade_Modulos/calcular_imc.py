from mod_continuar import deseja_continuar, leia_int, leia_float

def classificar_imc(imc):
    if imc < 18.5: return "Abaixo do peso"
    elif imc < 25.0: return "Peso normal"
    elif imc < 30.0: return "Sobrepeso"
    elif imc < 35.0: return "Obesidade Grau I"
    elif imc < 40.0: return "Obesidade Grau II"
    else: return "Obesidade Grau III"

def rotina_imc():
    print("--- Calculadora de IMC (Padrão UNIMED) ---")
    nome = input("Nome do paciente: ").strip()
    
    # Validação automática via módulo
    idade = leia_int("Idade: ")
    peso = leia_float("Peso (kg): ")
    altura = leia_float("Altura (m): ")

    imc = peso / (altura ** 2)
    
    print("\n" + "="*40)
    print(f"📋 PACIENTE: {nome}")
    print(f"• IMC: {imc:.2f} ({classificar_imc(imc)})")
    print("="*40 + "\n")

if __name__ == "__main__":
    loop_ativo = True
    while loop_ativo:
        rotina_imc()
        loop_ativo = deseja_continuar("Deseja realizar um novo cálculo? (S/N): ")
