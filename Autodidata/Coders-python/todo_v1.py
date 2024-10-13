#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar Prato'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar Prato']
    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
