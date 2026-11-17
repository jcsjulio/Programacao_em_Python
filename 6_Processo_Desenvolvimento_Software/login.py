import mod_msg, mod_inputs
USUARIO = "JULIO"
SENHA = "123456"

def valida_usuario(user):
    while True:
        usuario = mod_inputs.recebe_str("Digite seu usuario: ")
        if len(usuario) >=5:
            if user == usuario:
                break
        else:
            print("O usuario ddeve ter 5 caracteres")
    return usuario

def valida_senha(senha1):
    while True:
        senha = mod_inputs.recebe_senha("Digite sua senha: ")
        if senha == senha1:
            break
        else:
            print("Erro: Senha incorreta! Tente novamente.\n")
    return senha



def main():
    mod_msg.msg_login_ini()
    usuario_validado = valida_usuario(USUARIO)
    print("Sucesso! o Usuario é:" , usuario_validado)
    senha_validada = valida_senha(SENHA)
    print("Sucesso! o Usuario é:" , senha_validada)
    print("\nSucesso! Bem-vindo,", usuario_validado ,"!")