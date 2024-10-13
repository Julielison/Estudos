# Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
# Ao final, exiba as 3 matrizes (no formato de matriz).
#feito: ok
#corrigido: 
import random

linhas = 2
colunas = 3

a = [[None]*colunas for i in range(linhas)]
b = [[None]*colunas for i in range(linhas)]
c = [[None]*colunas for i in range(linhas)]

print('Matriz A:')
for i in range(linhas):
  for j in range(colunas):
    a[i][j] = random.randint(1,20)
    b[i][j] = random.randint(1,20)
    c[i][j] = a[i][j]+b[i][j]
    print(f'{a[i][j]:4}', end='')
  print()

print('Matriz B:')
for i in range(linhas):
  for j in range(colunas):
    print(f'{b[i][j]:4}', end='')
  print()

print('Matriz C:')
for i in range(linhas):
  for j in range(colunas):
    print(f'{c[i][j]:4}', end='')
  print()