class PilhaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

import numpy as np
'''
Metodos:
'''
class Pilha:
    def __init__(self, tamanho = 10) -> None:
        self.__array = np.full(tamanho, None)
        self.__tamanho = 0

    def __len__(self) -> int:
        return self.__tamanho

    def esta_vazia(self) -> bool:
        return self.__tamanho == 0

    def topo(self) -> any:
        if self.esta_vazia():
            raise PilhaError("Pilha está vazia")
        return self.__array[len(self)-1]

    def esta_cheia(self) -> bool:
        return len(self.__array) == self.__tamanho

    def elemento(self, posicao: int) -> any:
        try:
            assert 0 < posicao <= len(self)
        except AssertionError:
            raise PilhaError("Posição inválida")

        return self.__array[posicao-1]

    def busca(self, chave: any) -> int:
        if self.esta_vazia():
            raise PilhaError('Pilha esta vazia')
        
        for i in range(len(self)):
            if chave == self.__array[i]:
                return i+1

        raise PilhaError("Chave não encontrada")

    def empilha(self, carga: any) -> None:
        if self.esta_cheia():
            raise PilhaError("Pilha esta cheia")

        self.__array[len(self)] = carga
        self.__tamanho += 1

    def desempilha(self) -> any:
        if self.esta_vazia():
            raise PilhaError("Não há elementos para remover")

        self.__tamanho -= 1
        return self.__array[len(self)]

    def esvaziar(self) -> None:
        while not self.esta_vazia():
            self.desempilha()

    def __str__(self) -> str:
        s = '['
        for i in range(len(self)):
            s += f'{self.__array[i]}, '

        s += ']<-topo'
        return s

        