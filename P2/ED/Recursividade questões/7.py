# Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros positivos. Se n = 3, a soma seria igual a 1 + 2 + 3 = 6

def somaAtehN(n: int) -> int:
    if n == 1:
        return 1
    return somaAtehN(n-1) + n

n = 3
print(somaAtehN(n))

# Leia de cima pra baixo
'''
(3):
    return (2) + 3
        return (1) + 2
            return 1
'''

# Leia de baixo pra cima
'''
(3): -> 6
    return 3 + 3
        return 1 + 2
            return 1
'''