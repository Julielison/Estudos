class Processo:
    def __init__(self, nome: str, tempo_execucao: int, tempo_chegada: int) -> None:
        self.nome = nome
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.tempo_espera = 0
        self.tempo_conclusao = '-'
        self.status = 'ESPERANDO'
        self.turnaround = '-'
        self.tempo_inicio_execução = None
        self.tempo_executado = 0
        self.tempo_resposta = '-'


class Processos:
    processos = {}
    quantidade_processos = 0
    tempo_medio_espera = '-'
    throughput = None

    @classmethod
    def adicionar_processo(cls, processo: Processo, tempo_chegada) -> None:
        if tempo_chegada in cls.processos:
            cls.processos[tempo_chegada].append(processo)
        else:
            cls.processos[tempo_chegada] = [processo]
        cls.quantidade_processos += 1