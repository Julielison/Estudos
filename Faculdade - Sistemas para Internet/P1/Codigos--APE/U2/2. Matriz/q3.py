# Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se ordem elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0 (zero).
# Veja o exemplo a seguir:
#...
# Ao final, imprima as duas matrizes (no formato de matriz).
#feito: ok
#corrigido: 
import random

ordem = int(input('Ordem da matriz: '))
matriz_a = [[None]*ordem for i in range(ordem)]
matriz_b = [[None]*ordem for i in range(ordem)]

print('Matriz A:')
for i in range(ordem):
    for j in range(ordem):
        matriz_a[i][j] = random.randint(1,30)
        if (i == j) or (i + j == ordem - 1):
            matriz_b[i][j] = 0
        else:
            matriz_b[i][j] = matriz_a[i][j] + j+i
        print(f'{matriz_a[i][j]:4}', end='')
    print()

print('Matriz B:')
for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz_b[i][j]:4}', end='')
    print()