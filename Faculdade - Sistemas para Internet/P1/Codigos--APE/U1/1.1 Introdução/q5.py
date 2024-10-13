seg = int(input('Digite o número de segundos: '))
horas = seg//3600
resto_h = seg%3600
min = resto_h//60
segundos = resto_h%60
print(f'{seg}s equivale a {horas}h {min}min e {segundos}')