hodômetro_i = int(input('Hodômetro incial: '))
hodômetro_f = int(input('Hodômetro final: '))
litro_gasto = int(input('Combustível consumido: '))
preço_litro = float(input('Valor da gasolina: '))
capac_tanq = int(input('Capacidade do tanque: '))
km_rodado = hodômetro_f-hodômetro_i
km_litro = km_rodado/litro_gasto
autonomia = km_litro*capac_tanq
custo = litro_gasto*preço_litro
print(f'Km rodado: {km_rodado} km')
print(f'Eficiência: {km_litro:.1f} km/L')
print(f'Autonomia: {autonomia:.1f} km')
print(f'Custo da viagem: R$ {custo}')