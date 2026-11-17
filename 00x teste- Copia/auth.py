from utils import exibir_banner, ler_texto

# Credenciais padrão para acesso ao sistema (letras e números)
USUARIO_CADASTRADO = "admin123"
SENHA_CADASTRADA = "senai2025"

def realizar_login():
    while True:
        exibir_banner("COTAFRETE")
        print("--- BEM-VINDO AO SISTEMA DE COTAÇÃO ---")
        print("Faça login para continuar (use letras e números).\n")

        usuario = ler_texto("Usuário: ")
        senha = ler_texto("Senha: ")

        if not usuario.isalnum() or not senha.isalnum():
            print("\nErro: Usuário e senha devem conter apenas letras e números.")
            ler_texto("Pressione ENTER para tentar novamente...")
            continue

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            print("\nLogin realizado com sucesso! Carregando menu...")
            return True
        else:
            print("\nErro: Usuário ou senha incorretos!")
            ler_texto("Pressione ENTER para tentar novamente...")
