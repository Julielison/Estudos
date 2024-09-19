import csv
from processo import Processos, Processo
from cpu import CPU, limpar_terminal

def escolher_arquivo(nome_arquivo: str) -> None:
    # Carrega os processos na memória
    with open(f'./processos/{nome_arquivo}.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)
        for linha in leitor_csv:
            processo = Processo(linha[0], int(linha[2]), int(linha[1]))
            Processos.adicionar_processo(processo, processo.tempo_chegada)


def main():
    while True:
        print('''\
Escolha uma das opções de simulação:
1. CPU trabalhando até terminar
2. CPU ociosa no meio do caminho
3. Dois processos chegando ao mesmo tempo''')

        opcao = input('Digite: ')
        opcoes = {'1': 'normal', '2': 'cpu_ociosa', '3': 'tempo_chegada_igual'}
        if opcao in opcoes:
            escolher_arquivo(opcoes[opcao])
        else:
            limpar_terminal()
            print('Digite uma opção válida!')
            continue

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