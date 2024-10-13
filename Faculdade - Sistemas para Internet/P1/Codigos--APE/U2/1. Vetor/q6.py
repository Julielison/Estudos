#Escreva um programa que leia um vetor de N números inteiros (N será lido), inverta a ordem dos elementos do vetor e exiba o vetor invertido.
#Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
#Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!
#ok
n = int(input('Quantos números serão lidos: '))
v = [None]*n
c = [None]*n
print(f'Digite {n} números:')
for i in range(n):
    v[i] = int(input())
    c[i] = v[i]
for i in range(n):
    v[n-1-i] = c[i]
print(f'V = {v}')