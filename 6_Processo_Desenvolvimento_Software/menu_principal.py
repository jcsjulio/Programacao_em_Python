import mod_msg, mod_inputs, calculadora


def recebe_opcao():
    while True:
        mod_msg.msg_menu_principal2()
        opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
        match opcao:
            case 0:
                print("Sair do programa")
                break
            case 1:
                print("Aqui chamo calcular")
                calculadora.main()
            case 2:
                print("aqui chamo Calcular frete")
            case _:
                print("opção invalida")
def main():
    
    #mod_msg.msg_menu_principal2()
    recebe_opcao() 
