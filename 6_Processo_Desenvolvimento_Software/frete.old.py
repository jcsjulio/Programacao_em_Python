import mod_inputs
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()

ORIGEM = "Viracopos"

DESTINOS = {
    1: ("Congonhas-SP", 102),
    2: ("Guarulhos-SP", 112),
    3: ("Campo de Marte-SP", 98),
    4: ("Pinto Martins-CE", 2922),
    5: ("Eduardo Gomes-AM", 6294),

}


def exibir_aeroportos():
    tabela = Table(title="Tabela de Aeroportos x Distancia")
    tabela.add_column("Aeroporto de Origem", justify="center")
    tabela.add_column("Aeroporto de Destino")
    tabela.add_column("Distancia")

    destinos = list(DESTINOS.values())
    linha_central = len(destinos) // 2

    for indice, (nome, distancia) in enumerate(destinos):
        if indice == linha_central:
            origem = ORIGEM
        else:
            origem = ""
            
        tabela.add_row(origem, nome, f"{distancia} KM")


    console.print(tabela)


def escolher_destino():
    exibir_aeroportos()
    console.print("\n[bold]Escolha o aeroporto de destino:[/bold]")
    for numero, (nome, distancia) in DESTINOS.items():
        console.print(f"[cyan][{numero}][/cyan] {nome} - {distancia} KM")
    console.print("[red][0][/red] Voltar")

    while True:
        opcao = mod_inputs.recebe_int("Digite o numero do destino: ")
        if opcao == 0:
            return None
        if opcao in DESTINOS:
            return DESTINOS[opcao]
        console.print("[bold red]Opcao invalida! Escolha um destino de 1 a 5.[/bold red]")


def escolher_embalagem():
    console.print("\n[bold]Tipo de embalagem:[/bold]")
    console.print("[cyan][1][/cyan] Embalagem Caixa Papelao")
    console.print("[cyan][2][/cyan] Embalagem Container")
    console.print("[red][0][/red] Voltar")

    while True:
        opcao = mod_inputs.recebe_int("Digite o tipo de embalagem: ")
        if opcao in (0, 1, 2):
            return opcao
        console.print("[bold red]Opcao invalida! Escolha 1, 2 ou 0.[/bold red]")


def calcular_custo(tipo_embalagem, destino, distancia):
    if tipo_embalagem == 1:
        console.print("[bold]Embalagem Caixa Papelao[/bold]")
        console.print("Unidades: altura, largura e profundidade em metros.")
        altura = mod_inputs.recebe_float("Altura (m): ")
        largura = mod_inputs.recebe_float("Largura (m): ")
        profundidade = mod_inputs.recebe_float("Profundidade (m): ")
        fator = 0.26
    else:
        console.print("[bold]Embalagem Container[/bold]")
        console.print("Unidades: altura, largura e profundidade em centimetros.")
        altura = mod_inputs.recebe_float("Altura (cm): ") / 100
        largura = mod_inputs.recebe_float("Largura (cm): ") / 100
        profundidade = mod_inputs.recebe_float("Profundidade (cm): ") / 100
        fator = 0.37

    peso_real = mod_inputs.recebe_float("Peso (kg): ")

    # 1. Calcula o volume (m³) e o peso cubado (padrão rodoviário = 300)
    volume = altura * largura * profundidade
    peso_cubado = volume * 300

    # 2. A transportadora cobra pelo MAIOR peso (real ou cubado)
    peso_taxavel = max(peso_real, peso_cubado)

    # 3. Tarifa base (ex: R$ 0,02 por kg a cada km rodado)
    tarifa_km_kg = 0.02
    frete_base = peso_taxavel * distancia * tarifa_km_kg

    # 4. Aplica o fator de custo operacional (26% ou 37%)
    custo = frete_base * (1 + fator)

    detalhes = (
        f"[bold]Origem:[/bold] {ORIGEM}\n"
        f"[bold]Destino:[/bold] {destino}\n"
        f"[bold]Distancia:[/bold] {distancia} KM\n"
        f"[bold]Peso Real:[/bold] {peso_real:.2f} kg | [bold]Cubado:[/bold] {peso_cubado:.2f} kg\n"
        f"[bold]Peso Cobrado:[/bold] {peso_taxavel:.2f} kg\n"
        f"[bold]Fator operacional:[/bold] {fator:.2f}\n"
        f"[bold green]Custo do frete: R$ {custo:.2f}[/bold green]"
    )
    console.print(Panel(detalhes, title="Calculo do Frete", border_style="green", width=60, padding=(1, 4)))


def main():
    while True:
        console.print(Panel(
            "[bold cyan]Calculo de Frete[/bold cyan]\n"
            f"[bold]Aeroporto de origem:[/bold] {ORIGEM}",
            border_style="bright_blue"
        ))

        destino = escolher_destino()
        if destino is None:
            console.print("[yellow]Voltando ao menu principal...[/yellow]\n")
            break

        nome_destino, distancia = destino
        tipo_embalagem = escolher_embalagem()
        if tipo_embalagem == 0:
            console.print("[yellow]Voltando ao menu principal...[/yellow]\n")
            break

        calcular_custo(tipo_embalagem, nome_destino, distancia)

        continuar = mod_inputs.recebe_int("Deseja calcular outro frete? (1-Sim / 0-Nao): ")
        if continuar != 1:
            console.print("[yellow]Voltando ao menu principal...[/yellow]\n")
            break



if __name__ == "__main__":
    main()