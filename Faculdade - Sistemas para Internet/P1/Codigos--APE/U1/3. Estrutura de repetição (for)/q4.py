for i in range(3):
    n = int(input('Digite um n° inteiro: '))
    if i == 0:
        maior = n
    if n > maior:
        maior = n
print(f'O maior valor é {maior}')