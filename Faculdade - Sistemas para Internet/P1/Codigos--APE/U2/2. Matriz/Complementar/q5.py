#png
#feita: ok
#corrigida: 

m = [[None]*5 for i in range(5)]
#preenchendo a diagonal principal
for i in range(5):
    m[i][i] = 0

#Preenchendo a matriz manualmente de forma otimizada
#cont = 0
#for i in range(4):
#    for j in range(cont, 4):
 #       m[i][j+1] = m[j+1][i] = int(input()) #insira os dados à direita do "-" de cada linha na sequência
  #  cont+=1

#matriz já preenchida
m[0][1] = m[1][0] = 15
m[0][2] = m[2][0] = 30
m[0][3] = m[3][0] = 5
m[0][4] = m[4][0] = 12
m[1][4] = m[4][1] = 28
m[1][3] = m[3][1] = 17
m[1][2] = m[2][1] = 10
m[2][3] = m[3][2] = 3
m[2][4] = m[4][2] = 11
m[4][3] = m[3][4] = 80

#Calculando a distância com base no destino
dp = 0
ultimo = int(input('Local de partida (1-5): ')) - 1
while True:
        proximo = int(input('Destino (1-5 ou 0 p/ parar): '))
        if proximo == 0:
            break
        dp += m[ultimo][proximo-1]
        ultimo = proximo-1

print(f'Distância percorrida: {dp} km')
print('Matriz:')
for i in range(5):
    for j in range(5):
        print(f'{m[i][j]:4}', end='')
    print()