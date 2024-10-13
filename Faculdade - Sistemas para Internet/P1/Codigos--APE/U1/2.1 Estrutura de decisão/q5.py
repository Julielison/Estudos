from math import sqrt
while True: 
    a = float(input('Digite o valor de a: '))
    if a > 0:
        break
    else:
        print('a não pode ser negativo')
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = b**2 - 4*a*c
if delta >= 0:
    x1 = (-b - sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a
    if x1 != x2:
        print(f'x1 = {x1:.2f} e x2 = {x2:.2f}')
    else:
        print(f' x1 = x2 = {x1:.2f}')
else:
    print('Não há raiz real')