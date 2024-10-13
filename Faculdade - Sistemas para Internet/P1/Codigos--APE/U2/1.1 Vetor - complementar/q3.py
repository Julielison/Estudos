#Escreva um programa para ler 6 números. Após a leitura dos números, verifique, para cada um deles, se é distinto, ou seja, não possui repetição.
#ok
v = [None]*6
for i in range(6):
    v[i] = int(input(f'Digite o {i+1}º valor: '))
print('Os seguintes números não se repetem: ', end='')
for i in range(6):
    if v.count(v[i]) < 2:
        print(f'{v[i]}', end=', ')