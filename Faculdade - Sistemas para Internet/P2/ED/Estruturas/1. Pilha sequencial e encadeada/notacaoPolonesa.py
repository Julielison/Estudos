from pilhaEncadeada import Pilha
def calcula_expressao(expressao:str, dicio:dict):
    valores = Pilha()
    p = Pilha()
    for i in range(len(expressao)-1, -1, -1):
        p.empilha(expressao[i])
    
    while not p.esta_vazia():
        c = p.desempilha()
        if c.isalpha():
            valores.empilha(dicio[c])
        else:
            direita = valores.desempilha()
            esquerda = valores.desempilha()
            match(c):
                case '+':
                    valores.empilha(esquerda+direita)
                case '-':
                    valores.empilha(esquerda-direita)
                case '*':
                    valores.empilha(esquerda*direita)
                case '^':
                    valores.empilha(esquerda**direita)
                case '/':
                    valores.empilha(esquerda/direita)
    return valores.desempilha()

dicio = {'A': 5, 'B': 2, 'C': 2, "D": 1, "E": 4, "F": 2, "G": 3, "H": 2}
expressao = 'AB^C*D-EF/GH+/+'
result = calcula_expressao(expressao, dicio)
print(result)