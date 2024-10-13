# Uma certa empresa pretende verificar se os seus empregados estarão qualificados ou não para aposentadoria em 2022. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
#• Ter no mínimo 65 anos de idade; ou
#• Ter trabalhado no mínimo 30 anos; ou
#• Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
#Com base nas informações acima, faça um programa para:
#• Ler o nome do empregado, o ano de nascimento e o ano de seu ingresso na empresa.
#• Calcular e exibir a idade e o tempo de trabalho do empregado (estimado ao final de 2021)
#• Exibir a mensagem “Pode Requerer Aposentadoria” se atender aos requisitos ou “Não Pode Requerer Aposentadoria” caso contrário.
#Ao final de cada execução, o programa deverá perguntar se o usuário deseja fazer nova verificação. Se sim, o programa deverá repetir tudo novamente, caso contrário deverá encerrar.
#ok
verif = 's'
while verif == 's':
    nome = input('Digite seu nome: ')
    nascimento = int(input(f'Em que ano você nasceu?: '))
    ingresso = int(input('Em que ano você ingressou na empresa?: '))
    time_work = 2021-ingresso
    idade = 2021-nascimento
    print(f'Nome: {nome}\nIdade: {idade} anos\nTempo de trabalho: {time_work} anos')
    if idade >= 65 or time_work >= 30 or (idade>=60 and time_work>=25):
        print('Pode Requerer Aposentadoria')
    else:
        print('Não Pode Requerer Aposentadoria')
    verif = input('Deseja fazer outra verificação? (s/n): ').lower()
print('Fim')