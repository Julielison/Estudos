#Escreva um programa que leia um vetor A de N números inteiros (N será lido) e um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K. Ex: A = [1,2,3], K = 5, B = [5,10,15].
#ok
n = int(input('Quantos números serão lidos?: '))
k = int(input('Qual o valor de K?: '))
a = [None]*n
b = [None]*n
for i in range(n):
    a[i] = int(input('Quais os valores de A?: '))
    b[i] = a[i]*k
print(f'A = {a}\nB = {b}')
    