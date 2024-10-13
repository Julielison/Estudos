# 11) Faça uma função recursiva denominada seqTermos1() que calcule a soma dos n termos da série:
# n =    1    2     3     4     5           n
# série: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
# def seqTermos1(n), onde n é o número de termos:

def seqTermos1(n):
    if (n == 1):
        return 1    
    return seqTermos1(n-1) + 1/n

n = 5
soma = seqTermos1(n)
print(soma)


# Leia de cima pra baixo
'''
(5):
    return (4) + 1/5
        return (3) + 1/4
            return (2) + 1/3
                return (1) + 1/2
                    return 1
'''

# Leia de baixo pra cima
'''
(5): -> 2.28...
    return 2.08... + 1/5
        return 1.83... + 1/4
            return 1.5 + 1/3
                return 1 + 1/2
                    return 1
'''