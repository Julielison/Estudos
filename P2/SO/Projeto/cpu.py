from processo import *
from tabulate import tabulate
from util import limpar_terminal, exibir_erro

class CPU:
    fila_prontos = list()
    finalizados = list()
    estado = 'Trabalhando'

    @classmethod
    def exibir_painel(cls, cronometro):
        print('CPU status:', cls.estado)
        print('Timer:', cronometro, 'u')

    @classmethod
    def exibir_fila(cls) -> None:
        cabecalhos = ["NOME", "CHEGADA", "SERVIÇO", 'EXECUTADO', "ESPERA", "CONCLUSÃO", "TURNAROUND", 'RESPOSTA', 'STATUS']
        dados = []
        if len(cls.finalizados) > 0:
            for p in cls.finalizados:
                cls.adicionar_na_tabela(dados, p)

        if len(cls.fila_prontos) > 0:
            for p in cls.fila_prontos:
                cls.adicionar_na_tabela(dados, p)

        print(tabulate(dados, headers=cabecalhos, tablefmt="fancy_grid"))

    @classmethod
    def exibir_tudo(cls, tempo):
        limpar_terminal()
        cls.exibir_painel(tempo)
        cls.exibir_fila()

    @classmethod
    def adicionar_na_tabela(cls, dados, p: Processo) -> None:
        dados.append([p.nome, p.tempo_chegada, p.tempo_execucao, p.tempo_executado
                      , p.tempo_espera, p.tempo_conclusao, p.turnaround, p.tempo_resposta, p.status])

    @classmethod
    def carregar_processo(cls, tempo: int) -> None:
        lista = Processos.processos.get(tempo, [])
        for p in lista:
            cls.fila_prontos.append(p)

        # if len(cls.fila_prontos) > 0:
        #     if cls.fila_prontos[0].status == 'ESPERANDO':
        #         cls.fila_prontos[0].status = 'EXECUTANDO'
        #         cls.fila_prontos[0].tempo_inicio_execução = tempo
        #         cls.fila_prontos[0].tempo_resposta = p.tempo_inicio_execução - p.tempo_chegada
    
    @classmethod
    def executar_processo(cls):
        if len(cls.fila_prontos) > 0:
            p = cls.fila_prontos[0]
            p.tempo_executado += 1


    @classmethod
    def contar_espera(cls) -> None:
        prontos = cls.fila_prontos

        for i in range(1,len(prontos)):
            prontos[i].tempo_espera += 1


    @classmethod
    def finalizar_processo(cls, tempo):
        prontos = cls.fila_prontos

        if prontos:
            p = prontos[0]
            if p.tempo_executado == p.tempo_execucao:
                p.status = 'FINALIZADO'
                p.tempo_conclusao = tempo
                p.turnaround = tempo - p.tempo_chegada
                cls.finalizados.append(cls.fila_prontos.pop(0))

    @classmethod
    def atualiza_executando(cls, tempo):
        prontos = cls.fila_prontos
        
        if prontos:
            p = prontos[0]
            if p.status == 'ESPERANDO':
                p.status = 'EXECUTANDO'
                p.tempo_inicio_execução = tempo
                p.tempo_resposta = p.tempo_inicio_execução - p.tempo_chegada

    @classmethod
    def calcular_tempo_médio_espera(cls):
        media = 0
        finalizados = cls.finalizados
        if len(finalizados) > 0:
            for p in finalizados:
                media += p.tempo_espera

            media /= len(finalizados)
            Processos.tempo_medio_espera = media

    @classmethod
    def calcular_throughput(cls, tempo) -> None:
        Processos.throughput = len(cls.finalizados) / tempo


    @classmethod
    def exibir_metricas_finais(cls, tempo):
        if len(cls.finalizados) == 0 or tempo == 0:
            print('Sem dados para exibir!')
            return
        
        cls.calcular_tempo_médio_espera()
        cls.calcular_throughput(tempo)
        print('Dados dos processos finalizados:')
        print(f'Throughput: {Processos.throughput:.2f} p/u')
        print(f'Tempo médio de espera:', round(Processos.tempo_medio_espera, 2), 'u')


    @classmethod
    def restaurar_cpu(cls) -> None:
        cls.fila_prontos = list()
        cls.finalizados = list()
        cls.estado = 'Trabalhando'
        Processos.processos = {}
        Processos.quantidade_processos = 0
        Processos.tempo_medio_espera = '-'
        Processos.throughput = None

    @classmethod
    def escolher_modo_execução(cls) -> bool:
        limpar_terminal()
        while True:
            print('Escolha como o timer será passado:')
            print('1. Manual (melhor para entender o passo a passo)')
            print('2. Automático (mais prático)')
            opcao = input()

            match opcao:
                case '1':
                    return False
                case '2':
                    return True
                case _:
                    limpar_terminal()
                    exibir_erro()
                    continue