import {Language} from './language';

export class Languagepair {
    id : number;
    language_one : Language;
    language_two : Language;

    constructor(id : number, language_one : Language, language_two : Language){
        this.id = id;
        this.language_one = language_one;
        this.language_two = language_two;
    }
}