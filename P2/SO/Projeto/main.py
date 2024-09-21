from processo import Processo, Processos
from util import *
from cpu import CPU
import time
import csv

def selecionar_arquivo(nome_arquivo: str) -> None:
    # Carrega os processos na memória
    with open(f'./processos/{nome_arquivo}.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)
        for linha in leitor_csv:
            processo = Processo(linha[0], int(linha[2]), int(linha[1]))
            Processos.adicionar_processo(processo, processo.tempo_chegada)


'''
Algoritmo
Escolhe os processos que serão escalonados (pré-definidos)
Escolhe o modo de execução (automático ou manual)
'''


def main():
    limpar_terminal()
    while True:
        print('Bem-vindo(a) ao escalonador de processos FIFO')
        print('1. Executar processos pré-definidos')
        print('2. Inserir processos manualmente')

        escolha = input()

        match escolha:
            case '1':
                limpar_terminal()
                while True:
                    print('Escolha uma das categorias abaixo:')
                    print('1. CPU trabalhando até terminar')
                    print('2. CPU ociosa no meio do caminho')
                    print('3. Dois processos chegando ao mesmo tempo')

                    opcao = input()
                    opcoes = {'1': 'normal', '2': 'cpu_ociosa', '3': 'tempo_chegada_igual'}

                    if opcao in opcoes:
                        selecionar_arquivo(opcoes[opcao])
                        break
                    else:
                        limpar_terminal()
                        exibir_erro()
                        continue
        
            case '2':
                limpar_terminal()
                Processos.inserir_manualmente()
            case _:
                limpar_terminal()
                exibir_erro()
                continue

        automatico = CPU.escolher_modo_execução()

        tempo = 0
        while True:

            CPU.carregar_processo(tempo)
            CPU.atualiza_executando(tempo)

            if len(CPU.fila_prontos) == 0:
                CPU.estado = 'Ociosa'
            else:
                CPU.estado = 'Trabalhando'
            
            CPU.exibir_tudo(tempo)

            if len(CPU.finalizados) == Processos.quantidade_processos:
                break

            if automatico:
                time.sleep(1)
            else:
                op = input('x: sair\nEnter: continuar\n').lower()
                if op == 'x':
                        break

            tempo += 1

            CPU.contar_espera()
            CPU.executar_processo()
            CPU.finalizar_processo(tempo)
            CPU.atualiza_executando(tempo)
        
        CPU.exibir_metricas_finais(tempo)

        while True:
            opcao = input('1. Testar outros processos\nX. Sair\nDigite: ').lower()
            limpar_terminal()
            match opcao:
                case '1':
                    break
                case 'x':
                    return
                case _:
                    print('Digite uma opção válida!')
        CPU.restaurar_cpu()


if __name__ == '__main__':
    main()