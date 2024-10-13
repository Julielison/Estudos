# Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
#png
# Com base na definição apresentada, escreva um programa que preencha uma matriz quadrada com valores fornecidos pelo usuário, determine e mostre se ela é uma matriz de permutação.
#feita: ok
#corrigida: 

n = int(input('Ordem da matriz: '))
mtz = [[None]*n for i in range(n)]

print('Digite os elementos da matriz (o ou 1):')
for i in range(n):
    for j in range(n):
        mtz[i][j] = int(input())
        
cont = 0
for i in range(n):
    if mtz[i].count(1) == 1 and mtz[i].count(0) == n-1:
        coluna = mtz[i].index(1)
        for i in range(n):
            if mtz[i][coluna] == 1:
                cont +=1
    else:
        break
if cont == n:
    print('A matriz lida é de permutação')
else:
    print('A matriz lida não é de permutação')

for i in range(n):
    for j in range(n):
        print(f'{mtz[i][j]:4}', end='')
    print()