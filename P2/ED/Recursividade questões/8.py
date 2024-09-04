# Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor inferior a key. O protótipo da função é definido por:

def menores_rec(lista: list, key: int) -> int:
    if len(lista) == 0:
        return 0
    
    if lista[0] < key:
        return menores_rec(lista[1:], key) + 1
    else:
        return menores_rec(lista[1:], key)


lista = [1, 2, 3]
key = 4
print(menores_rec(lista, key))

# Leia de cima pra baixo
'''
([1, 2, 3], 4): 
    return ([2, 3]) + 1
        return ([3]) + 1
            return ([]) + 1
                return 0
'''

# Leia de baixo pra cima
'''
([1, 2, 3], 4): -> 3
    return 2 + 1
        return 1 + 1
            return 0 + 1
                return 0
'''