from rich.console import Console
from rich.panel import Panel
import limpatela
console = Console()

def exibir_menu_calc():
    opcoes = (
        "[bold cyan][1][/bold cyan] Somar (+)\n"
        "[bold cyan][2][/bold cyan] Subtrair (-)\n"
        "[bold cyan][3][/bold cyan] Multiplicar (*)\n"
        "[bold cyan][4][/bold cyan] Dividir (/)\n"
        "[bold cyan][5][/bold cyan] Porcentagem (%)\n"
        "[bold red][6][/bold red] Voltar ao Menu Principal"
    )
    painel = Panel(
        opcoes,
        title="[bold green]CALCULADORA[/bold green]",
        border_style="bright_blue",
        width=50,
        padding=(1, 4)
    )
    console.print(painel)

def ler_numero(mensagem):
    while True:
        try:
            # Aceita tanto ponto quanto vírgula para decimais
            valor = input(mensagem).replace(",", ".")
            return float(valor)
        except ValueError:
            console.print("[bold red]Entrada inválida! Digite um número válido.[/bold red]")

def main():
    while True:
        exibir_menu_calc()
        opcao = input("Escolha uma operação: ").strip()

        if opcao == "6":
            console.print("[yellow]Voltando ao Menu Principal...[/yellow]\n")
            break

        if opcao not in ("1", "2", "3", "4", "5"):
            console.print("[bold red]Opção inválida! Escolha de 1 a 6.[/bold red]\n")
            continue

        num1 = ler_numero("Digite o primeiro número: ")
        segundo_rotulo = "Digite a porcentagem: " if opcao == "5" else "Digite o segundo número: "
        num2 = ler_numero(segundo_rotulo)

        if opcao == "1":
            resultado = num1 + num2
            simbolo = "+"
        elif opcao == "2":
            resultado = num1 - num2
            simbolo = "-"
        elif opcao == "3":
            resultado = num1 * num2
            simbolo = "*"
        elif opcao == "4":
            if num2 == 0:
                console.print("[bold red]Erro: Não é possível dividir por zero![/bold red]\n")
                continue
            resultado = num1 / num2
            simbolo = "/"
        elif opcao == "5":
            resultado = num1 * num2 / 100

        if opcao == "5":
            texto_resultado = f"{num2}% de {num1}"
        else:
            texto_resultado = f"{num1:.2f} {simbolo} {num2:.2f}"

        console.print(
            Panel(
                f"[bold white]{texto_resultado} = [bold green]{resultado:.2f}[/bold green][/bold white]",
                title="Resultado",
                border_style="green",
                width=50
            )
        )
        print()

# Permite testar a calculadora sozinha se quiser

if __name__ == "__main__":
    main()
