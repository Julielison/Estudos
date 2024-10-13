#Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#• Os números que estão nos índices pares;
#• Os números que estão nos índices ímpares.
#ok, mas ineficiente
v = [None]*5
print('Digite 5 valores: ')
for i in range(5):
    v[i] = int(input())
print(f'Números dos índices pares: ', end='')
for i in range(5):
    if i%2 == 0:
        print(v[i], end=', ')
print(f'\nNúmeros dos índices ímpares: ', end='')
for i in range(5):
    if i%2 != 0:
        print(v[i], end=', ')