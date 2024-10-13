n = int(input('Digite um n° inteiro: '))
for c in range(n, 1, -1):
    if int(n**(1/2)) != n**(1/2):
        n -= 1
print(f'{n} é um quadrado perfeito')