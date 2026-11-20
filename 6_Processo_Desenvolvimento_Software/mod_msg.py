import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()

def msg_inicial():
    print("Seja bem-vindo ao Sistema")
    mensagem = pyfiglet.figlet_format("COTA - FRETE", font="slant")
    print(mensagem)

def msg_login_ini():
    print("###################################################################")
    print("######################## LOGAR NO SISTEMA #########################")
    print("###################################################################\n")


def msg_menu_principal():
    titulo = pyfiglet.figlet_format("MENU", font="small")
    print(titulo)
    print("╔══════════════════════════════════════════════════════════╗")
    print("║  [1] Calculadora   |   [2] Calcula Frete   |   [3] Sair  ║")
    print("╚══════════════════════════════════════════════════════════╝\n")


def msg_menu_principal2():
    opcoes = (
        "[bold cyan][1][/bold cyan] Calculadora\n"
        "[bold cyan][2][/bold cyan] Calcula Frete\n"
        "[bold red][0][/bold red] Sair"
    )
    
    painel_menu = Panel(
        opcoes,
        title="[bold green]MENU PRINCIPAL[/bold green]",
        subtitle="[dim]Escolha uma opção abaixo[/dim]",
        border_style="bright_blue",
        width=60,
        padding=(1, 4)
    )
    console.print(painel_menu)
    print()
