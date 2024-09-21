from util import limpar_terminal

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
    def adicionar_processo(cls, processo:Processo, tempo_chegada:int) -> None:
        if tempo_chegada in cls.processos:
            cls.processos[tempo_chegada].append(processo)
        else:
            cls.processos[tempo_chegada] = [processo]
        cls.quantidade_processos += 1

    @classmethod
    def inserir_manualmente(cls):
        while True:
            try:
                quantidade = int(input('Quantos processos deseja adicionar? '))
                assert quantidade > 0
            except:
                limpar_terminal()
                print('Digite um número natural maior que zero!')
                continue
            break


        for _ in range(quantidade):
            while True:
                print('Quantidade escolhida:', quantidade)
                print('Digite os dados do processo separados por espaço.')
                print('<nome> <tempo_chegada> <tempo_execução>')
                print('Exemplo: A 0 2')

                try:
                    nome, tempo_chegada, tempo_execução = input().split()
                except ValueError:
                    limpar_terminal()
                    print('Digite exatamente 3 argumentos separados por espaço!')
                    continue

                if nome == '':
                    limpar_terminal()
                    print('Digite um nome válido!')
                    continue

                try:
                    tempo_chegada = int(tempo_chegada)
                    tempo_execução = int(tempo_execução)
                except:
                    limpar_terminal()
                    print('Tempo de chegada e execução devem ser números!')
                    continue

                if tempo_chegada < 0:
                    limpar_terminal()
                    print('Tempo de chegada não pode ser negativo!')
                    continue
                elif tempo_execução < 1:
                    limpar_terminal()
                    print('Tempo de execução deve ser no mínimo 1!')
                    continue
                break
            
            cls.adicionar_processo(Processo(nome, tempo_execução, tempo_chegada), tempo_chegada)
            limpar_terminal()
            print('Processo adicionado ✅')