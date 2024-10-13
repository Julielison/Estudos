# Dado um vetor de números inteiro, escreva uma função recursiva para identificar o maior valor armazenado no vetor.

def maior_valor(vetor: list) -> int:
    if len(vetor) == 1:
        return vetor[0]
    
    if vetor[0] > vetor[-1]:
        return maior_valor(vetor[:-1])
    else:
        return maior_valor(vetor[1:])

vetor = [4, 1, 5, 3, 2]
maior = maior_valor(vetor)
print(maior)

# Leia de cima pra baixo
'''
([4, 1, 5, 3, 2]):
    return ([4, 1, 5, 3])
        return ([4, 1, 5])
            return ([1, 5])
                return ([5])
                    return 5
'''

# Leia de baixo pra cima
'''
([4, 1, 5, 3, 2]): -> 5
    return 5
        return 5
            return 5
                return 5
                    return 5
'''