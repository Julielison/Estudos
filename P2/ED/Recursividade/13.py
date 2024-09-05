# Dado um vetor de números reais, escreva uma função recursiva para determinar a soma dos elementos do vetor.

def soma_vetor(vetor: list) -> float:
    if len(vetor) == 0:
        return 0
    return soma_vetor(vetor[1:]) + vetor[0]

vetor = [1.2, 2.3, 3.4]
soma = soma_vetor(vetor)
print(soma)

# Leia de cima pra baixo
'''
([1.2, 2.3, 3.4]):
    return ([2.3, 3.4]) + 1.2
        return ([3.4]) + 2.3
            return ([]) + 3.4
                return 0
'''

# Leia de cima pra baixo
'''
([1.2, 2.3, 3.4]): -> 6.9
    return 5.7 + 1.2
        return 3.4 + 2.3
            return 0 + 3.4
                return 0
'''