from utils import exibir_banner, ler_int, ler_float, pausar

DESTINOS = {
    1: ("Congonhas-SP", 102),
    2: ("Guarulhos-SP", 112),
    3: ("Campo de Marte-SP", 98),
    4: ("Pinto Martins-CE", 2922),
    5: ("Eduardo Gomes-AM", 6294)
}

def executar_cotacao():
    exibir_banner("FRETE")
    print("--- COTAÇÃO DE FRETE (ORIGEM: VIRACOPOS) ---\n")
    print("Selecione o Aeroporto de Destino:")
    for codigo, (nome, dist) in DESTINOS.items():
        print(f" [{codigo}] {nome} ({dist} KM)")

    opcao_destino = ler_int("\nEscolha o destino (1 a 5): ", minimo=1, maximo=5)
    nome_destino, distancia = DESTINOS[opcao_destino]

    print("\nSelecione o Tipo de Embalagem:")
    print(" [1] Caixa de Papelão (Dimensões em Metros)")
    print(" [2] Container (Dimensões em Centímetros)")
    opcao_embalagem = ler_int("\nEscolha a embalagem (1 ou 2): ", minimo=1, maximo=2)

    if opcao_embalagem == 1:
        tipo_embalagem = "Caixa de Papelão"
        unidade = "m (Metros)"
        fator_custo = 0.26
    else:
        tipo_embalagem = "Container"
        unidade = "cm (Centímetros)"
        fator_custo = 0.37

    print(f"\nInforme as medidas da embalagem em {unidade}:")
    altura = ler_float(f" Altura ({unidade}): ")
    largura = ler_float(f" Largura ({unidade}): ")
    profundidade = ler_float(f" Profundidade ({unidade}): ")
    peso = ler_float(" Peso em Kg: ")
    total_itens = ler_int(" Total de Itens: ", minimo=1)

    # Aplicação da fórmula: ((Y * X * Z * W) * (1 + F)) * (1 + (D * 9.8))
    custo_unitario = ((altura * largura * profundidade * peso) * (1 + fator_custo)) * (1 + (distancia * 9.8))
    custo_total = custo_unitario * total_itens

    print("\n" + "=" * 50)
    print(" RESUMO DA COTAÇÃO")
    print("=" * 50)
    print(f" Origem:        Viracopos")
    print(f" Destino:       {nome_destino} ({distancia} KM)")
    print(f" Embalagem:     {tipo_embalagem}")
    print(f" Dimensões:     {altura} x {largura} x {profundidade} ({unidade})")
    print(f" Peso Unitário: {peso:.2f} Kg")
    print(f" Qtd. Itens:    {total_itens}")
    print("-" * 50)
    print(f" Frete Unitário: R$ {custo_unitario:,.2f}")
    print(f" VALOR TOTAL:    R$ {custo_total:,.2f}")
    print("=" * 50)

    pausar()
