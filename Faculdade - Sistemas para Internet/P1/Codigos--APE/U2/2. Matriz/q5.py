# Escreva um programa que:
#• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma turma e a média de cada um deles.
#   - As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
#   - As médias serão calculadas e armazenadas na 4a coluna da matriz.
#• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
#• Calcule e imprima a média geral da turma.
#• Calcule e imprima o número de alunos com média superior à média geral da turma.
#feito: ok
#corrigido: 

import random

LINHAS = 20
COLUNAS = 4
matriz = [[None]*COLUNAS for i in range(LINHAS)]
cont = soma_m = 0

print(' '*10,end='')
for j in range(COLUNAS-1):
    print(f' {j+1}ª NOTA ',end='')
print('  MÉDIA')

for i in range(LINHAS):
    print(f'{i+1:2}º ALUNO',end='')
    for j in range(COLUNAS-1):
        matriz[i][j] = random.randint(0, 10)
        print(f'{matriz[i][j]:9}', end='')
    matriz[i][3] = round((matriz[i][0] + matriz[i][1] + matriz[i][2])/3, 1)
    soma_m += matriz[i][3]
    print(f'{(matriz[i][3]):8}')

media = round(soma_m/20, 1)
print(f'Média geral: {media:.1f}')
for i in range(LINHAS):
    if matriz[i][COLUNAS-1] > media:
        cont+=1
print(f'Nº de alunos com média superior à média geral: {cont}')