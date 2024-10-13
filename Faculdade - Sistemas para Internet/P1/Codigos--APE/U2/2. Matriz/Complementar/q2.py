# Uma matriz quadrada contendo valores inteiros é denominada quadrado mágico quando a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico.
#png
# Escreva um programa que preencha uma matriz com valores fornecidos pelo usuário, determine e mostre se ela é um quadrado mágico.
#feita: ok
#corrigida: 
n = int(input('Ordem da matriz: '))
mtz = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        mtz[i][j] = int(input())

for i in range(n):
    cont_l = cont_c = cont_dp = cont_ds = 0
    for j in range(n):
        cont_l += mtz[i][j]
        cont_c += mtz[j][i]
        cont_dp += mtz[j][j]
        cont_ds += mtz[j][n-1-j]
    if cont_l == cont_ds == cont_dp == cont_c:
        qm = True
    else:
        qm = False
        print(f'Não é um quadrado mágico ;(')
        break

if qm == True:
    print(f'É um quadrado mágico!!!')