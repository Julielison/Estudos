nota1 = float(input('Digite sua primera nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1+nota2)/2
if média >= 7:
    print('Você foi aprovado na primeira etapa')
    nota3 = float(input('Digite sua terceira nota: '))
    if nota3 >= 8:
        print('Você foi aprovado no concurso!!!')
    else:
        print('Você foi reprovado na 2ª etapa')
else:
    print('Você foi reprovado na 1ª etapa')