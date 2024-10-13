#Escreva um programa que leia um vetor V contendo N elementos inteiros (N será lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver, informe em que posição (índice). Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K aparece.
#ok
n = int(input('Quantos números serão lidos? '))
v = [None]*n
print(f'Digite {n} valores: ')
for i in range(n):
    v[i] = int(input())
k = int(input('Qual número deseja verificar se está na lista? '))
print(f'{k} aparece em V nas seguintes posições: ', end='')
for i in range(n):
    if k == v[i]:
        print(i, end=', ')