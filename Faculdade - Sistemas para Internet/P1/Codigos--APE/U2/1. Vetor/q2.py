#Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
#ok
n = 5
v = [None]*n
cont = 0
print(f'Digite {n} valores: ')
for i in range(n):
    v[i] = int(input())
k = int(input('Digite o número que deseja verificar na lista: '))
for i in range(n):
    if k == v[i]:
        cont += 1
print(f'{k} aparece no vetor V {cont} vezes')
print(f'v = {v}')