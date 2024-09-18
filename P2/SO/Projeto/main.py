import csv
from processo import Processos, Processo
from cpu import CPU
import time

arquivo = './processos/normal.csv'

# Carrega os processos na memória
with open(arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        processo = Processo(linha[0], int(linha[2]), int(linha[1]))
        Processos.adicionar_processo(processo, processo.tempo_chegada)


def main():
    tempo = 0

    while True:
        CPU.carregar_processo(tempo)
        CPU.atualiza_executando(tempo)

        if len(CPU.fila_prontos) == 0:
            CPU.estado = 'Ociosa'
        else:
            CPU.estado = 'Trabalhando'
        
        CPU.exibir_tudo(tempo)
        if len(CPU.finalizados) == 5:
            break

        op = input('x: sair\nEnter: continuar\n')
        if op == 'x':
                break

        tempo += 1

        CPU.contar_espera()
        CPU.executar_processo()
        CPU.finalizar_processo(tempo)
        CPU.atualiza_executando(tempo)
    
    CPU.exibir_metricas_finais(tempo)

main()