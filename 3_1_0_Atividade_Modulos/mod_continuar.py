import mod_inputs 



def deseja_continuar(mensagem_confirmacao="Deseja continuar? (S/N): "):
    while True:
        opcao = mod_inputs.leia_str(mensagem_confirmacao).strip().upper()
        if opcao in ['S', 'SIM']:
            return True
        elif opcao in ['N', 'NAO', 'NÃO']:
            print("\nEncerrando o programa. Até mais!")
            return False
        else:
            print("Opção inválida! Por favor, digite S para Sim ou N para Não.")

