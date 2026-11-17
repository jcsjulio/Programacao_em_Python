import getpass

def recebe_str(mensagem):
    while True:
        try:
            texto = str(input(mensagem))
            if len(texto) >= 5:
                break
            else:
                print("Sua senha deve ter no minimo 5 caracteres")
        except:
            print("Valor Invalido!")
    return texto

def recebe_senha(mensagem):
    while True:
        try:
            #senha = str(input(mensagem))
            senha = getpass.getpass(mensagem)
            if len(senha) >= 5:
                return senha
            #break
            else:
                print("Erro: A senha deve ter no mínimo 5 caracteres (letras e números).")
        except:
            print("Valor invalido!")
    return senha