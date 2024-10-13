#Escreva um programa que receba um vetor V de N números inteiros (N será lido), determine e exiba o maior e o menor elemento deste vetor e seus respectivos índices. Obs: suponha a inexistência de valores repetidos.
#ok
n = int(input('Quantos números serão lidos? '))
v = [None]*n
print(f'Digite {n} números:')
menor = maior = v[0] = int(input())
for i in range(n-1):
    v[i] = int(input())
    if v[i] < menor:
        menor = v[i]
    elif v[i] > maior:
        maior = v[i]
print(f'Maior elemento da lista: {maior}\nMenor elemento da lista: {menor}')