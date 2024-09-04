# Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário.

def printInverse(string: str) -> None:
    if string == '':
        return
    
    printInverse(string[1:])
    print(string[0], end='')

palavra = 'teste'
printInverse(palavra)

'''
await print(t) -> (este)
    await print(e) -> (ste)
        await print(s) -> (te)
            await print(t) -> (e)
                await print(e) -> ('')
                    return None
'''