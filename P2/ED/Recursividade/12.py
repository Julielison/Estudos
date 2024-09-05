# Faça uma função recursiva denominada seqTermos2() que calcule a soma dos n termos da série:
# 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... + (n^2 + 1)/(n + 3)

# Soma impar começando em 3 no numerador e 1 no denominador

def seqTermos2(n: int) -> float:
    if n == 1:
        return 2/4
    return seqTermos2(n-1) + (n**2 + 1)/(n+3)

n = 5
soma = seqTermos2(n)
print(soma)

# Leia de cima pra baixo
'''
(5):
    return (4) + 26/8
        return (3) + 17/7
            return (2) + 10/6
                return (1) + 5/5
                    return 2/4
'''

# Leia de baixo pra cima
'''
(5): -> 8.84...
    return 5.59... + 26/8
        return 3.16... + 17/7
            return 1.5 + 10/6
                return 2/4 + 5/5
                    return 2/4
'''