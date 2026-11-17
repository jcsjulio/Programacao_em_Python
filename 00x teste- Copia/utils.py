import os
import sys
import pyfiglet

class SairDoSistema(Exception):
    """Exceção usada para encerrar o programa de qualquer tela."""
    pass

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner(texto="COTAFRETE"):
    limpar_tela()
    banner = pyfiglet.figlet_format(texto, font="slant")
    print("=" * 65)
    print(banner)
    print("=" * 65)
    print(" Dica: Digite 'SAIR' a qualquer momento para encerrar o sistema.")
    print("=" * 65 + "\n")

def ler_texto(mensagem):
    entrada = input(mensagem).strip()
    if entrada.upper() == "SAIR":
        raise SairDoSistema()
    return entrada

def ler_float(mensagem, permitir_zero=False):
    while True:
        try:
            entrada = ler_texto(mensagem).replace(",", ".")
            valor = float(entrada)
            if not permitir_zero and valor <= 0:
                print("Erro: O valor deve ser maior que zero.\n")
                continue
            return valor
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números.\n")

def ler_int(mensagem, minimo=None, maximo=None):
    while True:
        try:
            entrada = ler_texto(mensagem)
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"Erro: O número deve ser no mínimo {minimo}.\n")
                continue
            if maximo is not None and valor > maximo:
                print(f"Erro: O número deve ser no máximo {maximo}.\n")
                continue
            return valor
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.\n")

def pausar():
    ler_texto("\nPressione ENTER para continuar (ou digite SAIR)...")
