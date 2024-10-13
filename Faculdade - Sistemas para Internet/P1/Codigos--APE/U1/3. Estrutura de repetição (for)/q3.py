n = int(input('Digite um número: '))
produto = 1
for i in range(1, n+1):
    produto *= i
print(f'O fatorial de {n} é {produto}')