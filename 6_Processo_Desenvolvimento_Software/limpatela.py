import os
import subprocess


def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)