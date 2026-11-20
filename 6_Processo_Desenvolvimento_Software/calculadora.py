from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_menu_calc():
    opcoes = (
        "[bold cyan][1][/bold cyan] Somar (+)\n"
        "[bold cyan][2][/bold cyan] Subtrair (-)\n"
        "[bold cyan][3][/bold cyan] Multiplicar (*)\n"
        "[bold cyan][4][/bold cyan] Dividir (/)\n"
        "[bold red][5][/bold red] Voltar ao Menu Principal"
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

        if opcao == "5":
            console.print("[yellow]Voltando ao Menu Principal...[/yellow]\n")
            break

        if opcao not in ("1", "2", "3", "4"):
            console.print("[bold red]Opção inválida! Escolha de 1 a 5.[/bold red]\n")
            continue

        num1 = ler_numero("Digite o primeiro número: ")
        num2 = ler_numero("Digite o segundo número: ")

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

        console.print(
            Panel(
                f"[bold white]{num1} {simbolo} {num2} = [bold green]{resultado:.2f}[/bold green][/bold white]",
                title="Resultado",
                border_style="green",
                width=50
            )
        )
        print()

# Permite testar a calculadora sozinha se quiser
if __name__ == "__main__":
    main()
