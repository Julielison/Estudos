import Exame from "./Exame.js"

// Definindo o gabarito e os pesos
const gabarito = ['a', 'b', 'a', 'c', 'd']
const pesos = [2, 2, 2, 2, 2]

// Instanciando um exame
const exame1 = new Exame(gabarito, pesos)

// Listas de respostas
const respostas1 = ['a', 'b', 'b', 'b', 'b'] // 4
const respostas2 = ['a', 'a', 'a', 'a', 'a'] // 4
const respostas3 = ['c', 'c', 'b', 'a', 'a']; // 0
const respostas4 = ['b', 'b', 'c', 'c', 'c']; // 4
const respostas5 = ['a', 'b', 'a', 'a', 'b']; // 6
const respostas6 = ['c', 'b', 'c', 'c', 'c']; // 4
const respostas7 = ['b', 'a', 'b', 'a', 'b']; // 0
const respostas8 = ['c', 'a', 'a', 'a', 'a']; // 2
const respostas9 = ['b', 'a', 'a', 'b', 'b']; // 2
const respostas10 = ['a', 'b', 'a', 'c', 'd']; // 10

// Adicionando respostas
exame1.add(respostas1);
exame1.add(respostas2);
exame1.add(respostas3);
exame1.add(respostas4);
exame1.add(respostas5);
exame1.add(respostas6);
exame1.add(respostas7);
exame1.add(respostas8);
exame1.add(respostas9);
exame1.add(respostas10);

// Exibe uma lista de todas as notas
console.log(`\nLista de todas as notas:`, exame1.notas())

// Exibe a quantidade de notas
console.log('\nQuantidade de notas:', exame1.qtd())

// Exibe a soma de todas as notas
console.log('\nSoma das notas:', exame1.soma())

// Exibe uma lista das notas menores que 5
console.log('\nNotas menores que 5:', exame1.menoresQue(5))

// Exibe uma lista das notas maiores que 4
console.log('\nNotas maiores que 4:', exame1.maioresQue(4))

// Exibe uma lista das menores notas (4 notas)
console.log("\n4 menores notas", exame1.min(4))

// Exibe uma lista das 5 maiores notas
console.log("\n5 maiores notas", exame1.max(5))

// Exibe a menor nota
console.log('\nA menor nota:', exame1.min())

// Exibe a maior nota
console.log('\nA maior nota:', exame1.max())

// Exibe a média de todas as notas
console.log('\nMédia das notas:', exame1.avg())