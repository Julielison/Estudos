# Jogo da Forca em Python
#### Video Demo:  <URL HERE>

Este é um jogo clássico da forca implementado em Python. O jogo desafia os jogadores a adivinharem uma palavra oculta por meio de palpites de letras. Cada jogador acumula pontos a cada letra correta e tem um número limitado de tentativas antes de perder o jogo.

## Funcionamento

1. **Menu Inicial:**
   - Ao iniciar o jogo, os jogadores são apresentados a um menu com duas opções: Jogar (1) ou Sair (2).

2. **Cadastro de Jogadores:**
   - Os jogadores são solicitados a fornecer um apelido válido para identificação no jogo.

3. **Carregamento de Dados:**
   - O jogo verifica se o apelido já existe no banco de dados. Se existir, carrega os dados do jogador, incluindo pontuação e palavras já adivinhadas. Caso contrário, cria um novo registro.

4. **Seleção de Palavra:**
   - Uma palavra é escolhida aleatoriamente a partir de um banco de palavras, e uma dica correspondente é fornecida.

5. **Jogabilidade:**
   - Os jogadores tentam adivinhar a palavra, fornecendo letras como palpites.
   - Cada letra correta revela sua posição na palavra, enquanto letras incorretas aumentam o número de erros.

6. **Desenhando o Boneco:**
   - A cada erro, uma parte do "boneco na forca" é desenhada, visualizando o progresso do jogador.

7. **Fim do Jogo:**
   - O jogo continua até que o jogador acerte a palavra, atinja o número máximo de erros (6), ou decida encerrar voluntariamente.
   - Ao final, a pontuação é exibida, e os dados do jogador são atualizados no arquivo de dados.

8. **Zerando o Jogo:**
   - Se o jogador acertar a última palavra do banco, o jogo é considerado "zerado", e os dados do jogador são removidos.

## Arquivos do Projeto

1. **project.py:**
   - Contém a lógica principal do jogo e funções utilizadas para gerenciar jogadores, palavras, e a execução do jogo.

2. **test_project.py:**
   - Arquivo com testes unitários para as funções principais do jogo, ajudando a garantir a robustez e correção do código.

## Executando o Jogo

Certifique-se de ter o Python instalado em seu sistema. Para jogar, execute o arquivo `project.py`, copie o código abaixo, cole no seu console e aperte Enter.

```bash
python project.py
```
Siga as instruções no console para interagir com o jogo.
