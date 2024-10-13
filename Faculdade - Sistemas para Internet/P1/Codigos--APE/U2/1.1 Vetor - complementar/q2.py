#Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos elementos de A e B.
#Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
#ok
n = int(input('Quantos números serão lidos pra cada vetor?: '))

vetor_a = [None]*n
vetor_b = [None]*n
vetor_c = [None]*2*n

print('Valores de A:')
for i in range(n):
    vetor_a[i] = int(input(f'Digite o {i+1}º valor: '))
    vetor_c[2*i] = vetor_a[i]
    
print('Valores de B:')
for i in range(n):
    vetor_b[i] = int(input(f'Digite o {i+1}º valor: '))
    vetor_c[2*i+1] = vetor_b[i]
print(f'Vetor C = {vetor_c}')