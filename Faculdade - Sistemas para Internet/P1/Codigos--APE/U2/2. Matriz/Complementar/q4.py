# Uma análise dos acidentes de trânsito está sendo realizada em Manhattan, New York. Os cruzamentos das ruas 30 a 38 com as avenidas 1a a 10a foram estudadas.
# Faça um programa para, a partir da informação acima, processar a matriz de acidentes resultante desse estudo.
# Para cada acidente, será informado o local do cruzamento (Avenida x Rua). O programa deverá ler um número desconhecido de acidentes (utilize qualquer condição de parada a sua escolha).
# Ao final da leitura dos dados, o programa deverá gerar e exibir a matriz de acidentes (obs: exiba na matriz os cabeçalhos de linha e de coluna mostrando a identificação das ruas e das avenidas)
#feita: 
#corrigida: 
L = 10
C = 9
m = [[0]*C for i in range(L)]

while True:
  av = int(input('Avenida (1-10) ou 0 to stop: '))
  if av == 0:
    break
  rua = int(input('Rua (30-38): '))
  m[av-1][rua-30] += 1

print('MAPA DOS ACIDENTES')
print('RUAS  30  31  32  33  34  35  36  37  38')
for i in range(L):
    print(f'AV{i+1:2}', end='')
    for j in range(C):
       if m[i][j] == 0:
          m[i][j] = '-'
       print(f'{m[i][j]:>4}', end='')
    print()