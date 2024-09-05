# Um material radioativo denominado invictus, quando em contato com o oxigênio, perde metade de sua massa a cada 50 segundos. Faça uma função recursiva que receba uma quantidade de massa do invictus, em gramas, e exiba o tempo (em segundos) necessário para que sua massa se torne menor que 0,8 g. A função também deve retornar o valor da massa final.

# Função para uso
def meiaVidaInvictus(massa: float) -> float:
    return __meiaVidaInvictus(massa)

# Função real privada
def __meiaVidaInvictus(massa: float, tempo = 0) -> float:
    if massa < 0.8:
        print('Tempo:', tempo, 'segundos')
        return massa
    
    tempo += 50
    return __meiaVidaInvictus(massa/2, tempo)

massa_inicial = 5
massa_final = meiaVidaInvictus(massa_inicial)
print('Massa:', massa_final, 'g')

# Leia de cima pra baixo
'''
(5, 0):
    return (2.5, 50)
        return (1.25, 100)
            return (0.625, 150)
                print(150)
                return 0.625
'''

# Leia de baixo pra cima
'''
(5, 0): -> 0.625
    return 0.625
        return 0.625
            return 0.625
                print(150)
                return 0.625
'''