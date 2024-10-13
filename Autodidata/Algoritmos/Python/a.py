# 1 é não ordenado
# 2 é ordenado
def soma_sub(l, lo, t, p, i, f, tudo):
    soma = 0
    if i == 0 and f+1 == t:
        return tudo

    if p == 1:
        for n in range(i, f+1):
            soma += l[n]
    else:
        for n in range(i, f+1):
            soma += lo[n]

    return soma
#
tm = int(input())
lista = list(map(int, input().split()))
lista_ord = sorted(lista)
tudo = 0
for e in lista:
    tudo += e

n = int(input())
for _ in range(n):
    p, i, f = map(int, input().split())
    print(soma_sub(lista, lista_ord, tm, p, i-1, f-1, tudo))