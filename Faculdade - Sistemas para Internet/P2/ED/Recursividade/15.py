# Dado um vetor de números inteiros, escreva uma função recursiva para verificar se um vetor está ordenado ou não.

# Obs: ordem crescente
def verificar_se_vetor_ordenado(vetor: list) -> bool:
    if len(vetor) == 1:
        return True
    
    if vetor[0] < vetor[1]:
        return verificar_se_vetor_ordenado(vetor[1:])
    return False

vetor = [1, 2, 3]
resultado = verificar_se_vetor_ordenado(vetor)
print(resultado)

# Leia de cima pra baixo
'''
([1, 2, 3]):
    return ([2, 3]):
        return ([3]):
            return True
'''

# Leia de baixo pra cima
'''
([1, 2, 3]): -> True
    return True
        return True
            return True
'''