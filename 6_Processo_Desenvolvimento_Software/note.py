from rich.console import Console
from rich.panel import Panel


console = Console()


Tabela de Aeroportos x Distância



Aeroporto de Origem
Viracopos

Aeroporto de Destino Distância

Congonhas-SP 102KM
Guarulhos-SP 112KM
Campo de Marte-SP 98KM
Pinto Martins-CE 2922KM
Eduardo Gomes-AM 6294KM



CÁLCULO PARA CUSTO DE FRETE:
Embalagem Caixa Papelão
Y = Altura em Mt (Metros)
X = Largura em Mt (Metros)
Z = Profundidade em Mt (Metros)
W = Peso em Kg (Kilo)
F = Fator de Custo Operacional (0.26)
D = Distância (KM)

FÓRMULA =((Y^ * X^ * Z^ * W)^ * (1 + F) )^ * (1+(D^ * 9.8))


Embalagem Container
Y = Altura em cm (centímetros)
X = Largura em cm (centímetros)
Z = Profundidade em cm (centímetros)
W = Peso em Kg (Kilo)
F = Fator de Custo Operacional (0.37)
D = Distância (KM)

FÓRMULA =((Y^ * X^ * Z^ * W)^ * (1 + F) )^ * (1+(D^ * 9.8))
  