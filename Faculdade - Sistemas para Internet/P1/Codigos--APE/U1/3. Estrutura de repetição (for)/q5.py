n = int(input('Digite o n° de pessoas: '))
h = 0
m = 0
for i in range(n):
    sexo = input('Digite seu sexo (M/F): ').upper()
    if sexo == 'M':
        h += 1
    else:
        m += 1
print(f'O percentual de homens é: {(h/n)*100} %')
print(f'O percentual de mulheres é: {(m/n)*100} %')