# Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada matriz.
# Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].
#png
# Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as duas matrizes (no formato de matriz).
#feito: ok
#corrigido: 

import random
m = 3
n = 5
matriz_c = [[None]*n for j in range(m)]
matriz_t = [[None]*m for j in range(n)]
print('Matriz C:')
for i in range(m):
    for j in range(n):
        matriz_c[i][j] = random.randint(1, 20)
        print(f'{matriz_c[i][j]:4}', end='')
    print()
print('Matriz Ct')
for i in range(n):
    for j in range(m):
        matriz_t[i][j] = matriz_c[j][i]
        print(f'{matriz_t[i][j]:4}', end='')
    print()