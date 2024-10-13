hodometro_antes = float(input('Digite a marcação do hodômetro antes da viagem: '))
hodômetro_depois = float(input('Digite a marcação do hodômetro depois da viagem: '))
litros_gastos = float(input('Digite a quantidade de litros de combustível gastos na viagem: '))
preço_litro = float(input('Digite o preço do litro de combustível: '))
capacidade_tanque = float(input('Digite a capacidade do tanque de combustível do carro: '))
quilometragem_rodada = hodômetro_depois - hodometro_antes
quilometros_por_litro = quilometragem_rodada/litros_gastos
autonomia_veiculo = quilometros_por_litro*capacidade_tanque
custo_viagem = preço_litro*litros_gastos
print(f'A quilometragem rodada do carro foi {quilometragem_rodada}km, o carro faz {quilometros_por_litro}km por litro, a autonomia do veiculo é de {autonomia_veiculo}km e o custo da viagem foi de {custo_viagem} reais.')