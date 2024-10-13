from project import *

def test_esconde_letras():
    assert esconde_letras('ARROZ') ==  '*****'
    assert esconde_letras('CAMPINA GRANDE') == '*******-******'

def test_marcar_chute_correto():
    assert marcar_chute_correto('ARROZ', 'A', '*****') ==  'A****'
    assert marcar_chute_correto('CAMPINA GRANDE', 'C', '*******-******') == 'C******-******'

def test_acertou():
    assert acertou('A****') == False
    assert acertou('ARROZ') == True