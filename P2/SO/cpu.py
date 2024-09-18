from processo import *
from tabulate import tabulate
import os


class CPU:
    fila_prontos = list()
    finalizados = list()
    estado = 'Trabalhando'

    @classmethod
    def exibir_painel(cls, cronometro):
        print('CPU status:', cls.estado)
        print('Timer:', cronometro)

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

        print(tabulate(dados, headers=cabecalhos, tablefmt="grid"))

    @classmethod
    def exibir_tudo(cls, tempo):
        os.system('cls')
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
            if len(cls.fila_prontos) > 0:
                cls.fila_prontos[0].status = 'EXECUTANDO'
    
    @classmethod
    def executar_processo(cls, tempo):
        if len(cls.fila_prontos) > 0:
            p = cls.fila_prontos[0]
            p.tempo_executado += 1

            if p.tempo_executado == p.tempo_execucao:
                p.status = 'FINALIZADO'
                p.tempo_conclusao = tempo
                p.turnaround = tempo - p.tempo_chegada
                cls.finalizados.append(cls.fila_prontos.pop(0))
                if len(cls.fila_prontos) > 0:
                    cls.fila_prontos[0].status = 'EXECUTANDO'

    @classmethod
    def contar_espera(cls) -> None:
        prontos = cls.fila_prontos

        for i in range(1,len(prontos)):
            prontos[i].tempo_espera += 1

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
        Processos.throughput = Processos.quantidade_processos / tempo

    @classmethod
    def exibir_metricas_finais(cls, tempo):
        cls.calcular_tempo_médio_espera()
        cls.calcular_throughput(tempo)
        print('Dados dos processos finalizados:')
        print(f'Throughput: {Processos.throughput} p/s')
        print(f'Tempo médio de espera:', Processos.tempo_medio_espera)