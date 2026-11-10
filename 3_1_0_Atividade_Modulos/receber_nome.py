from mod_continuar import deseja_continuar
from mod_inputs import leia_int, leia_float, leia_str
def executar_cadastro():
    print("--- Cadastro de Usuário ---")
    
    # Agora tudo é validado automaticamente pelo módulo!
    nome = leia_str("Digite seu nome completo: ")
    idade = leia_int("Digite sua idade: ")
    peso = leia_float("Digite seu peso (kg): ")

    print("\n" + "="*35)
    print(f"FICHA CADASTRAL: {nome.upper()}")
    print(f"• Idade: {idade} anos")
    print(f"• Peso: {peso:.2f} kg")
    print("="*35 + "\n")

if __name__ == "__main__":
    loop_ativo = True
    while loop_ativo:
        executar_cadastro()
        loop_ativo = deseja_continuar("Deseja realizar um novo cadastro? (S/N): ")
