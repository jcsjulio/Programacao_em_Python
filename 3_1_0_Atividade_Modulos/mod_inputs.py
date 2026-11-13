def leia_int(mensagem):
    
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("❌ Erro! Por favor, digite um número inteiro válido.")

def leia_float(mensagem):
    
    while True:
        try:
            # Substitui vírgula por ponto para o Python conseguir converter
            valor = float(input(mensagem).replace(',', '.'))
            return valor
        except ValueError:
            print("❌ Erro! Por favor, digite um número decimal válido.")

def leia_str(mensagem):
    
    while True:
        valor = input(mensagem).strip()  # .strip() remove espaços inúteis no início e fim
        if valor == "":                  # Verifica se ficou vazio após remover os espaços
            print("❌ Erro! O campo não pode ficar em branco. Por favor, digite algo.")
        else:
            return valor

