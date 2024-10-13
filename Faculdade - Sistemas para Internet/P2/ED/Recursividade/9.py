# Faça uma função recursiva chamada decToBin() que receba um número inteiro na base decimal e imprima seu correspondente na base binária. O protótipo da função é definido por:

# def decToBin( num: int ) -> None:
#     resto = num % 2

#     if num == 1 or num == 0:
#         return f'{resto}'
    
#     return decToBin(num//2) + f'{resto}'

# n = 5
# print(decToBin(n))

'''
(2):
    return '1' + '0'
        return '1'
'''

'''
(5): -> '0101'
    return '010' + 1
        return '01' + '0'
            return '0' + '1'
                return '0'
'''

# Funciona apenas para inteiros positivos
def decToBin( num: int ) -> None:
    resto = num % 2

    if num == 0:
        return
    
    decToBin(num//2)
    print(resto, end='')

n = 5
decToBin(n)

# leia as chamadas de cima pra baixo e os prints de baixo pra cima
'''
(5):
    await print(1, end='')
    (2):
        await print(0, end='')
        (1):
            await print(1, end='')
            (0):
                return
'''