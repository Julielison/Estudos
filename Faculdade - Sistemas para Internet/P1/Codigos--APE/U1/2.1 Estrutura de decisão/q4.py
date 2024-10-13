h_inicial = int(input('Hora inicial: '))
h_final = int(input('Hora final: '))
if h_final <= h_inicial:
    sub = 24 - h_inicial
    print(f'Você jogou durante {sub+h_final} horas')
else:
    print(f'Você jogou durante {h_final-h_inicial} horas')