hamburguer = c_burguer = c_bacon = c_frango = 0
código = input('Digite o código do pedido (B/C/F/H/X): ').upper()
while código != 'X':
    qtd = int(input('Qts você deseja?: '))
    if código == 'B':
        c_bacon += 7*qtd
    elif código == 'C':
        c_burguer += 6*qtd
    elif código == 'F':
        c_frango += 4*qtd
    else:
        hamburguer += 5*qtd
    código = input('Deseja algo mais? (B/C/F/H/X): ').upper()
print(f'Total a pagar: R$ {c_bacon+c_burguer+c_frango+hamburguer},00')