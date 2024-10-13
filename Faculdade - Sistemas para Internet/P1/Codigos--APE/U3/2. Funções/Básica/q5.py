def identidade(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if i == j and matriz[i][j] != 1:
        return False
      elif i != j and matriz[i][j] != 0:
        return False
  return True

result = identidade([[1,0,0],[0,1,0],[0,0,1]])
print('Identidade' if result else 'Não identidade')

ordem = 3
matriz = [[None]*ordem for i in range(ordem)]
for i in range(ordem):
    for j in range(ordem):
      matriz[i][j] = int(input())

result = identidade(matriz)
print('Identidade' if result else 'Não identidade')