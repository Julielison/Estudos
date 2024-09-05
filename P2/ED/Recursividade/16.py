# O código abaixo imprime, de forma recursiva, o Triângulo de Pascal. De acordo com o programa, qual a sequência numérica a ser impressa para cada iteração do comando for inserido no programa principal?

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

# Aqui se inicia o programa principal
for i in range(1,6):
    print(pascal(i))

# Leia de cima pra baixo
'''
(1):
    print([1])
    fim
(2):
    await line 8
    (1):
        return [1]
'''
#
'''
(1):
    [1]
    fim
(2):
    line = [1]
    previous_line = [1]
    return [1,1]
'''
# Resultado do for até o 2
'''
[1]
[1, 1]
'''
# i = 3
'''
(3):
    (2):
        (1):
            return [1]
'''
'''
(3): -> [1, 2, 1]
    previous = [1, 1]
    [1, 2, 1]
'''
# Resultado até o i = 3
'''
[1]
[1, 1]
[1, 2, 1]
'''
# Dedução* até o 5
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
'''
# * melhor acompanhar até o final