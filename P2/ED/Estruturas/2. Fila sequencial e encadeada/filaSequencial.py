import numpy as np

class FilaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class Fila:
    '''
    Classe que implementa a estrutura de dados Fila usando a 
    técnica sequencial circular
    '''
    def __init__(self, tamanho:int = 10):
        self.__array = np.full(tamanho,None)
        self.__fim = -1
        self.__inicio = 0
        self.__ocupados = 0

    def __len__(self)->int:
        return self.__ocupados

    def esta_vazia(self):
        return self.__ocupados == 0

    def frente(self)->any:
        '''
        Método que retorna a carga armazenada na frente da fila
        '''
        if self.esta_vazia():
            raise FilaError('Fila está vazia')
        return self.__array[self.__inicio]

    def esta_cheia(self):
        return self.__ocupados == len(self.__array)
    
    def elemento(self, posicao:int)->any:
        '''
        Método que recebe a posição de um elemento da fila que deseja
        consultar. Retorna a carga armazenada na posição específica.
        A posicao retornada é em direção da base para o topo
        '''
        try:
            assert  0 < posicao <= self.__ocupados
            index = self.__inicio
            for _ in range(posicao-1):
                index = (index + 1) % len(self.__array) 
            return self.__array[index]
        except AssertionError:
            raise FilaError(f'Posicao invalida. A fila no momento possui {len(self)} elementos.')

    def busca(self, chave:any)->int:
        '''
        Método que recebe uma chave de busca e retorna a posição em
        que a carga foi encontrada na fila
        '''
        index = self.__inicio
        for i in range(1,self.__ocupados + 1 ):
            if chave == self.__array[index]:
                return i
            index = (index + 1) % len(self.__array)
        raise FilaError(f"Chave {chave} não encontrada")

    def enfileira(self, carga:any):
        if self.esta_cheia():
            raise FilaError('Fila está cheia')
        self.__ocupados += 1
        self.__fim = (self.__fim + 1) % len(self.__array)
        self.__array[self.__fim] = carga

    def desenfileira(self)->any:
        if self.esta_vazia():
            raise FilaError('Fila está vazia')
        carga = self.__array[self.__inicio] 
        self.__inicio = (self.__inicio + 1 ) % len(self.__array)
        self.__ocupados -= 1
        return carga
        
    def esvaziar(self):
        while not self.esta_vazia():
            self.desenfileira()
            
    def __str__(self)->str:
        s = 'inicio->[ '

        index = self.__inicio
        for _ in range(self.__ocupados):
            s += f'{self.__array[index]}, '
            index = (index + 1 ) % len(self.__array)
        s = s.strip(', ')
        s += ' ]<-fim'
        return s