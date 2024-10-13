# Escreva um programa que preencha uma matriz quadrada de ordem 3 com valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente), calcule e exiba:
#• A soma dos elementos de cada linha;
#• A soma dos elementos de cada coluna;
#• A soma dos elementos da diagonal principal da matriz;
#• A soma dos elementos da diagonal secundária da matriz;
#• A soma de todos os elementos da matriz.
#feita: ok
#corrigida: 
import random
no = 3
m = [[None]*no for i in range(no)]
sm = 0

print('Matriz:')
for i in range(no):
    for j in range(no):
        m[i][j] = random.randint(1,10)
        sm += m[i][j]
        print(f'{m[i][j]:3}', end='')
    print()

cds = cdp = 0
for i in range(no):
    cl = cc = 0
    for j in range(no):
        cl += m[i][j]
        cc += m[j][i]
    cdp += m[i][i]
    cds += m[i][no-1-i]
    print(f'Soma da {i+1}ª linha = {cl}')
    print(f'Soma da {i+1}ª coluna = {cc}')

print(f'Soma da diagonal principal = {cdp}')
print(f'Soma da diagonal secundária = {cds}')
print(f'Soma dos elementos da matriz = {sm}')