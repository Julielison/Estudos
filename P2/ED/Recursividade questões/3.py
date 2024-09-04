# Faça uma função recursiva chamada invertString() que retorne a sequência de caracteres de uma string passada como argumento na ordem inversa

def invertString(string: str) -> str:
    if len(string) == 1:
        return string
    
    return invertString(string[1:]) + string[0]

palavra = 'nome'
print(invertString(palavra))

# Leia de cima pra baixo
'''
(teste):
    return (este) + 't'
        return (ste) + 'e'
            return (te) + 's'
                return (e) + 't'
                    return e
'''

# Leia de baixo pra cima
'''
(teste): -> 'etset'
    return 'etse' + 't'
        return 'ets' + 'e'
            return 'et' + 's'
                return 'e' + 't'
                    return e
'''