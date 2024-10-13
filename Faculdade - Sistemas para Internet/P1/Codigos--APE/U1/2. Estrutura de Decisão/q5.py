total_de_vendas = float(input('Digite quanto você vendeu: '))
comissão = total_de_vendas*00.5
if comissão>1320:
    print(f'Seu salário será R$ {comissão}')
else:
    print(f'Seu salário será R$ 1320,00')