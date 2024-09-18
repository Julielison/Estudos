# from pilhaSequencial import Pilha,PilhaError
# from pilhaSequencialImpl import Pilha,PilhaError
from pilhaEncadeada import Pilha,PilhaError
# from myPilhaEncad import Pilha,PilhaError

p = Pilha()
print('Len(p)', len(p))
try:
    for numero in range(10):
        p.empilha((numero+1)*10)
    print('Len(p)', len(p))
    print(p)
    # p.esvaziar()
    print(p)
    print('Elemento:', p.elemento(5))
    print('Busca:', p.busca(105))
    input('Pressione enter para desempilhar')

    for i in range(15):
        print(p.desempilha())
    print('Len(p)', len(p))
    print(p)
    print(p.__dict__)
except PilhaError as pe:
    print(pe)