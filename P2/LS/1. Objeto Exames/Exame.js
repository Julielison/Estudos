class Exame {
    // Guarda o gabarito, os pesos e uma lista de exames inicialamente vazia
    constructor(gabarito, pesos) {
        this.gabarito = gabarito
        this.pesos = pesos
        this.exames = []
    }

    // Adiciona as respostas de um exame à lista de exames
    add(respostas){
        this.exames.push(respostas)
    }

    // Extra: retorna uma lista de todas as notas
    notas() {
        // Define a pontuação de cada questão pra cada lista de respostas
        let pontuações = []
        this.exames.forEach( (respostas) => pontuações.push(respostas.map( (e, i) => this.gabarito[i] === e ? this.pesos[i]:  0)))

        // Definindo as notas em cada exame
        let notas = []
        pontuações.forEach( (pontuação) => notas.push( pontuação.reduce( (acc, e) => acc + e, 0 )))

        return notas
    }

    // Retorna a quantidade de notas
    qtd(){
        return this.exames.length
    }

    // Extra: retorna a soma de todas as notas
    soma() {
        const soma = this.notas().reduce( (acc, e) => acc + e)
        return soma
    }
    // Retorna a média das notas nos exames
    avg(){
        // Retorna a soma das notas
        const soma = this.soma()

        // Faz a média
        const média = soma / this.qtd()

        return média
    }

    // Retorna uma lista das menores notas em ordem crescente
    min(qtd = 1){
        const notasCrescente = this.notas().sort( (a, b) => a - b)
        return notasCrescente.splice(0, qtd)
    }

    // Retorna uma lista das maiores notas em ordem decrescente
    max(qtd = 1){
        const notasCrescente = this.notas().sort((a, b) => a - b)
        return notasCrescente.reverse().splice(0, qtd)
    }

    // Retorna uma lista das notas menores que o valor passado
    menoresQue(parâmetro){
        const notas = this.notas()
        return notas.filter( (e) => e < parâmetro)
    }

    // Retorna uma lista das notas maiores que o valor passado
    maioresQue(parâmetro){
        const notas = this.notas()
        return notas.filter( (e) => e > parâmetro)
    }
}

export default Exame