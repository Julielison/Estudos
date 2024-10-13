import random

# Menu jogar/sair e validar input
def jogar():
    inicio_fim = input('1) Jogar\n2) Sair\n')
    if inicio_fim == '2':
        return False
    elif inicio_fim != '1':
        print('Digite 1 ou 2!')
        return jogar()
    return True

# Retorna o histórico de dados do jogador se o apelido for encontrado na base de dados, se não, retorna os dados zerados
def verificar_apelido(apelido):
    linha_jogador = 0
    with open('dados_dos_jogadores.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            apelido_salvo, pontuação, palavras_adv = linha.split(';')
            if apelido_salvo == apelido:
                return apelido.strip(), int(pontuação), palavras_adv.upper().rstrip('\n'), linha_jogador
            linha_jogador += 1
        return apelido.strip(), int(0),'',-1

# Retorna a palavra, a dica e uma flag sinalizando se a última palavra foi sorteada
def carrega_palavra_dica(palavras_adv):
    ultima = False
    with open('banco_de_palavras.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        qtd_palavras_adv = len(palavras_adv.split())
        qtd_palavras = len(linhas)

        while qtd_palavras > qtd_palavras_adv:
            palavra, dica = random.choice(linhas).strip().split(';')
            if palavra.upper() in palavras_adv:
                continue
            if qtd_palavras == len(palavras_adv.split('.')) + 1:
                ultima = True
            return palavra.upper(), dica, ultima

    return None, None, ultima

# Troca cada letra da palavra por um *
def esconde_letras(palavra):
    palavra = palavra.replace(' ','-')
    for letra in palavra:
        if letra != '-':
            palavra = palavra.replace(letra, '*')
    return palavra

# Verifica se o chute foi repetido ou é inválido
def validar_chute(chute,chutes):
    if len(chute) > 1 or chute == '':
        print('Chute inválido!')
        return True
    elif chute in chutes:
        print('Letra repetida! Digite outra!')
        return True
    return False

#Funçâo para marcar o chute correto
def marcar_chute_correto(palavra, chute, palavra_secreta):
    palavra_secreta_at = ''
    index = 0
    for letra in palavra:
        if chute == letra:
            palavra_secreta_at += letra
        else:
            palavra_secreta_at += palavra_secreta[index]
        index += 1
    return palavra_secreta_at

# Verifica se a palavra foi adivinhada
def acertou(palavra_secreta):
    return '*' not in palavra_secreta

# Verifica se o arquivo está vazio ou não
def arquivo_esta_vazio():
    with open('dados_dos_jogadores.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        return not conteudo

#Atualiza o arquivo de dados
def atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador):
    palavras_adv_se = palavras_adv.strip('.')

    if linha_jogador >= 0: # excuta caso o jogador esteja no arquivo dados
        with open('dados_dos_jogadores.txt', 'r+', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            linhas[linha_jogador] = f'{apelido};{pontuação};{palavras_adv_se}\n'
            # remove o \n caso a linha  a ser alterada seja a última do arquivo
            if linha_jogador == len(linhas) - 1:
                linhas[linha_jogador] = linhas[linha_jogador].rstrip('\n')
            arquivo.seek(0)
            arquivo.writelines(linhas)

    else: # caso o jogador não tenha sido encontrado
        with open('dados_dos_jogadores.txt', 'a', encoding='utf-8') as arquivo:
            if arquivo_esta_vazio():
                arquivo.write(f'{apelido};{pontuação};{palavras_adv_se}')
            else:
                arquivo.write(f'\n{apelido};{pontuação};{palavras_adv_se}')

# Apaga os dados do jogador caso ele tenha zerado o jogo
def apaga_jogador(linha_jogador):
    with open('dados_dos_jogadores.txt', 'r+', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)
        if len(linhas) - 1 == linha_jogador:
            # remove o \n da linha anterior à última
            linhas[linha_jogador-1] = linhas[linha_jogador-1].rstrip('\n')
        del linhas[linha_jogador]
        arquivo.writelines(linhas) # sobrescreve as linhas
        arquivo.truncate() # remove o que há depois da última linha escrita

# Verifica se a última palavra sorteada foi acertada
def zerou_jogo(ultima,apaga,pontuação,linha_jogador):
    if ultima and apaga:
        print('Parabéns! Você zerou o jogo!')
        print(f'Pontuação final: {pontuação}')
        apaga_jogador(linha_jogador)
        print('Jogo encerrado!')
        return True
    return False

# Desenha o boneco na forca
def desenhar_boneco(erros):
    if erros == 1:
        print('┌────┐')
        print('│   😐')
        print('│')
        print('│')
        print('│')
    elif erros == 2:
        print('┌────┐')
        print('│   😐')
        print('│   ╱')
        print('│')
        print('│')
    elif erros == 3:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░')
        print('│')
        print('│')
    elif erros == 4:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│')
        print('│')
    elif erros == 5:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│   ╱')
        print('│')
    else:
        print('┌────┐')
        print('│   😐')
        print('│   ╱░╲')
        print('│   ╱ ╲')
        print('│')
        print('Você perdeu!')

def main():
    while jogar(): # Inicia ou sai do jogo
        print('Bem-vindo(a) ao Jogo da Forca')
        while True: # Pedir e validar o apelido
            apelido = input('Digite um apelido: ')
            if ';' in apelido or apelido == '':
                print('Apelido inválido! O apelido está vazio ou com ;')
                continue
            break

        while True: # Carrega os dados do jogador e da palavra
            apelido, pontuação, palavras_adv,linha_jogador = verificar_apelido(apelido)
            palavra, dica, ultima = carrega_palavra_dica(palavras_adv)

            if palavra == None: # Verifica se o jogador zerou o jogo sem jogar
                print('Dados inseridos manualmente!')
                apaga_jogador(linha_jogador) # apaga os dados do jogador
                break

            # Retorna a palavra com *
            palavra_secreta = esconde_letras(palavra)
            pontos = erros = 0
            chutes = ''
            acertada = False

            # Roda até que os erros cheguem a 6 ou a palavra seja acertada
            while erros < 6:
                print(f'\nDica: {dica}')
                print(palavra_secreta)
                chute = input('Qual a letra? ').upper()
                if validar_chute(chute,chutes):
                    continue
                chutes += chute

                if chute in palavra: # verifica se o usuário acertou o chute
                    palavra_secreta = marcar_chute_correto(palavra, chute, palavra_secreta)
                    pontos += 10
                    if acertou(palavra_secreta): # verifica se acertou a palavra
                        print('Parabéns, você acertou!!!')
                        print(f'A palavra era {palavra}')
                        palavras_adv += f'.{palavra}' # atualiza as palavras adivinhadas
                        pontuação += pontos
                        print(f'Pontos acumulados: {pontuação}')
                        acertada = True
                        atualiza_dados(apelido,pontuação,palavras_adv,linha_jogador)
                        break
                else:
                    erros += 1
                    print(f'Você errou {erros} de 6 tentativas')
                    desenhar_boneco(erros)

            # Verifica se o usuário zerou o jogo
            if zerou_jogo(ultima,acertada,pontuação,linha_jogador):
                break

            # Pergunta se o usuário quer seguir ou não
            segue = input('Deseja continuar? (s/n) ').lower()
            if segue == 's':
                continue
            print(f'Sua pontuação até aqui: {pontuação}')
            print(f'Jogo Encerrado!')
            break
        break

if __name__ == "__main__":
    main()