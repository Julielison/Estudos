n = int(input('Digite um n° inteiro: '))
while int(n**(1/2)) != n**(1/2):
        n -= 1
print(f'{n} é um quadrado perfeito')