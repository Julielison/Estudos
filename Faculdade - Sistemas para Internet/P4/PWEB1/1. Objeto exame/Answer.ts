export class Answer {
    name: string;
    responses: string[];

    constructor(name: string, responses: string[]) {
        this.name = name;
        this.responses = responses;
    }
}