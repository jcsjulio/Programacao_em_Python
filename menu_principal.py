import mod_msg, mod_inputs, calculadora, frete, limpatela



def recebe_opcao():
    while True:
        limpatela.limpar_tela()
        mod_msg.msg_inicial()
        mod_msg.msg_menu_principal2()
        opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
        match opcao:
            case 0:
                print("Sair do programa")
                break
            case 1:
                limpatela.limpar_tela()
                mod_msg.msg_inicial()
                calculadora.main()
            case 2:
                limpatela.limpar_tela()
                mod_msg.msg_inicial()
                frete.main()
            case _:
                limpatela.limpar_tela()
                mod_msg.msg_inicial()
                print("opção invalida")
def main():
    
    #mod_msg.msg_menu_principal2()
    recebe_opcao() 
