import os

def exibir_erro():
    print('Digite uma opção válida!')



def limpar_terminal():
    # Verifica se o sistema é Windows
    if os.name == 'nt':
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux e macOS