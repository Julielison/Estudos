dia = int(input('Digite o número do dia da semana (1-7): '))
if dia == 1:
    sem = 'Domingo'
    ops = 'é final de semana'
elif dia == 2:
    sem = 'Segunda'
    ops = 'é dia útil'
elif dia == 3:
    sem = 'Terça'
    ops = 'é dia útil'
elif dia == 4:
    sem = 'Quarta'
    ops = 'é dia útil'
elif dia == 5:
    sem = 'Quinta'
    ops = 'é dia útil'
elif dia == 6:
    sem = 'Sexta'
    ops = 'é dia útil'
else:
    sem = 'Sábado'
    ops = 'é final de semana'
print(sem, ops)