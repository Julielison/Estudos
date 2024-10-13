#Escreva um programa que leia um vetor contendo N elementos inteiros (N será lido), calcule e exiba:
#• A quantidade de elementos pares;
#• A quantidade de elementos ímpares;
#• A soma de todos os elementos;
#• A média dos elementos do vetor.
#ok
n = int(input('Quantos elementos serão lidos?: '))
v = [None]*n
pares = ímpares = soma = qtd = 0
for i in range(n):
  v[i] = int(input(f'Digite o {i+1}º valor: '))
  if v[i]%2 == 0:
    pares += 1
  else:
    ímpares += 1
  soma += v[i]
  qtd += 1
print(f'N° de elementos pares: {pares}\nN° de elementos ímpares: {ímpares}\nSoma de todos os elementos: {soma}\nMédia dos elementos do vetor: {soma/qtd:.2f}')