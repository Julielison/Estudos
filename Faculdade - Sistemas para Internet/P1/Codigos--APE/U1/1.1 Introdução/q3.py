x = int(input('digite um valor: '))
y = int(input('digite outro valor: '))
print(f'x = {x} e y = {y}')
z = x
x = y
y = z
print(f'Agora x = {x} e y = {y}')