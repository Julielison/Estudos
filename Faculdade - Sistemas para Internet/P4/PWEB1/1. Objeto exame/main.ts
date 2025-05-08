import { Exam } from './Exam';
import { Answer } from './Answer';
import { Weight } from './Weight';

// Gabarito e pesos
const gabarito = new Answer("gabarito", ['a', 'b', 'a', 'c', 'd']);
const pesos = new Weight([2, 2, 2, 2, 2]);

const exame = new Exam(gabarito, pesos);

// Respostas dos alunos
const respostas = [
    new Answer("Aluno1", ['a', 'b', 'b', 'b', 'b']), // 4
    new Answer("Aluno2", ['a', 'a', 'a', 'a', 'a']), // 4
    new Answer("Aluno3", ['c', 'c', 'b', 'a', 'a']), // 0
    new Answer("Aluno4", ['b', 'b', 'c', 'c', 'c']), // 4
    new Answer("Aluno5", ['a', 'b', 'a', 'a', 'b']), // 6
    new Answer("Aluno6", ['c', 'b', 'c', 'c', 'c']), // 4
    new Answer("Aluno7", ['b', 'a', 'b', 'a', 'b']), // 0
    new Answer("Aluno8", ['c', 'a', 'a', 'a', 'a']), // 2
    new Answer("Aluno9", ['b', 'a', 'a', 'b', 'b']), // 2
    new Answer("Aluno10", ['a', 'b', 'a', 'c', 'd']), // 10
];

respostas.forEach(resp => exame.add(resp));

console.log("Notas:", exame.calculateScores());
console.log("Média:", exame.avg());
console.log("Menores notas:", exame.min(4));
console.log("Maiores notas:", exame.max(5));
console.log("Notas < 5:", exame.lt(5));
console.log("Notas > 4:", exame.gt(4));
