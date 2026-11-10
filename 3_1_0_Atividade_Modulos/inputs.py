import mod_inputs 
import mod_continuar 

start = True
while start:

    nome = mod_inputs.leia_str("Digite seu nome completo: ")
    idade = mod_inputs.leia_int("Digite sua idade: ")
    peso = mod_inputs.leia_float("Digite seu peso (kg): ")

    print("\ndados informados")
    print("seu nome e", nome)
    print("voce possui", idade, "anos")
    print("seu peso ", peso ,"kg\n")


    start = mod_continuar.deseja_continuar("Deseja realizar um novo cadastro? (S/N): ")


# if __name__ == "__main__":
#    loop_ativo = True
#    while loop_ativo:
#        executar_cadastro()
#        loop_ativo = deseja_continuar("Deseja realizar um novo cadastro? (S/N): ")