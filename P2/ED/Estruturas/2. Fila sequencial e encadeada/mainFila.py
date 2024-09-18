# from filaSequencial import Fila, FilaError
from filaEncadeada import Fila, FilaError

f = Fila()
print('Len(f)', len(f))
try:
    for numero in range(9):
        f.enfileira((numero+1)*10)
    print('Len(f)', len(f))
    print(f)
    # f.esvaziar()
    print(f)
    print('Elemento:', f.elemento(3))
    print('Busca:', f.busca(180))
    input('Pressione enter para desenfileirar')

    for i in range(15):
        print(f.desenfileira())
    print('Len(f)', len(f))
    print(f)
    print(f.__dict__)
except FilaError as fe:
    print(fe)