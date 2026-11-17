from utils import exibir_banner, ler_int, SairDoSistema
from auth import realizar_login
from frete import executar_cotacao
from calculadora import executar_calculadora

def menu_principal():
    while True:
        exibir_banner("COTAFRETE")
        print("--- MENU PRINCIPAL ---\n")
        print(" [1] Cotação de Frete")
        print(" [2] Calculadora")
        print(" [0] Sair do Sistema")

        opcao = ler_int("\nEscolha uma opção: ", minimo=0, maximo=2)

        if opcao == 1:
            executar_cotacao()
        elif opcao == 2:
            executar_calculadora()
        elif opcao == 0:
            raise SairDoSistema()

def iniciar_sistema():
    try:
        if realizar_login():
            menu_principal()
    except (SairDoSistema, KeyboardInterrupt):
        print("\n\nEncerrando o sistema COTAFRETE. Até logo!")

if __name__ == "__main__":
    iniciar_sistema()
