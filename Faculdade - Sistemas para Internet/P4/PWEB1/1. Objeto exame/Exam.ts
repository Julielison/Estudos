import { Weight } from './Weight';
import { Answer } from './Answer';

export class Exam {
    private weight: Weight;
    private answer: Answer;
    private exams: Answer[];

    constructor(answer: Answer, weight: Weight) {
        this.answer = answer;
        this.weight = weight;
        this.exams = [];
    }

    add(exam: Answer): void {
        this.exams.push(exam);
    }

    calculateScores(): number[] {
        const scores: number[] = [];

        for (const exam of this.exams) {
            let total = 0;

            for (let i = 0; i < this.answer.responses.length; i++) {
                if (exam.responses[i] === this.answer.responses[i]) {
                    total += this.weight.scores[i];
                }
            }

            scores.push(total);
        }

        return scores;
    }

    avg(): number {
        const scores = this.calculateScores();
        const sum = scores.reduce((acc, val) => acc + val, 0);
        return scores.length ? sum / scores.length : 0;
    }

    min(count: number = 1): number[] {
        return this.calculateScores().sort((a, b) => a - b).slice(0, count);
    }

    max(count: number = 1): number[] {
        return this.calculateScores().sort((a, b) => b - a).slice(0, count);
    }

    lt(limit: number): number[] {
        return this.calculateScores().filter(score => score < limit);
    }

    gt(limit: number): number[] {
        return this.calculateScores().filter(score => score > limit);
    }
}
