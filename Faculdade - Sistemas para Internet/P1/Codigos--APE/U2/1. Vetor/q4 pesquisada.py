#Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#• Os números que estão nos índices pares;
#• Os números que estão nos índices ímpares.
#ok
n = 10
v = [None]*n
print(f'Digite {n} valores: ')
for i in range(n):
    v[i] = int(input())
print(f'Números nos índices pares: {v[:n:2]}') #lista[:parada:passo] ou lista[0:parada:passo] imprimirá os itens do começo da lista de 2 em 2 até (parada - 1)
print(f'Números nos índices ímpares: {v[1:n:2]}')