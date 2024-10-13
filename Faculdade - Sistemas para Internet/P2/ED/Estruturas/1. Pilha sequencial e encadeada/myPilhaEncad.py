class PilhaError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class No:
    def __init__(self, carga: any):
        self.carga = carga
        self.proximo = None

    def __str__(self) -> str:
        return f'{self.carga}'

class Pilha:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def __len__(self) -> int:
        return self.tamanho

    def esta_vazia(self) -> bool:
        return self.tamanho == 0

    def topo(self) -> any:
        if self.esta_vazia():
            raise PilhaError("Pilha vazia")

        return self.head.carga

    def elemento(self, posicao: int) -> any:
        # Retorna a carga daquela posicao"

        if self.esta_vazia():
            raise PilhaError("Pilha vazia")
        cursor = self.head

        for _ in range(len(self)-posicao):
            cursor.proximo

        return cursor.carga

    def busca(self, chave: any) -> int:
        if self.esta_vazia():
            raise PilhaError("Pilha vazia")
        
        cursor = self.head
        p = len(self)
        while (cursor != None):
            if chave == cursor.carga:
                return p
            cursor = cursor.proximo
            p -= 1 
        raise PilhaError('Chave não encontrada')

    def empilha(self, carga: any) -> None:
        no = No(carga)
        no.proximo = self.head
        self.head = no
        self.tamanho += 1

    def desempilha(self) -> any:
        if self.esta_vazia():
            raise PilhaError('Pilha vazia')

        carga = self.head.carga
        self.head = self.head.proximo
        self.tamanho -= 1
        return carga
    
    def esvaziar(self) -> any:
        while not self.esta_vazia():
            self.desempilha()

    def __str__(self) -> str:
        s = 'topo->['
        cursor = self.head
        while (cursor != None):
            s += f'{cursor.carga}, '
            cursor = cursor.proximo
        s = s.rstrip(', ')
        s += ']'
        return s