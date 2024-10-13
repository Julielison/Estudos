nome = input('Nome do vendedor: ')
n_carros = int(input('Número de carros vendidos: '))
total_vendas = float(input('Total de vendas: '))
SALÁRIO = 1000
COMISSÃO = 200
salario_total = SALÁRIO+COMISSÃO*n_carros+total_vendas*0.05
print(f'{nome} vendeu {n_carros} carros, o total de vendas foi R$ {total_vendas} e ele recebeu R$ {salario_total} de salário')