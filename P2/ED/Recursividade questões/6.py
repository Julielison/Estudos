# Faça uma função recursiva chamada ispalindrome() que retorne verdadeiro caso uma string seja palíndrome, ou falso caso contrário. O protótipo da operação é definido por:

def invertString(string: str) -> str:
    if len(string) == 1:
        return string
    
    return invertString(string[1:]) + string[0]

def ispalindrome(string: str) -> bool:
    if string == invertString(string):
        return True
    return False

palavra = 'arara'
print(ispalindrome(palavra))