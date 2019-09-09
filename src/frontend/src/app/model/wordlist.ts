import { WordPair } from "./wordpair";
import { Language } from "./language";

export class WordList {
    id : number;
    name : string;
    first_language : Language;
    second_language : Language;
    wordpairs : WordPair[];

    constructor(id : number, name : string, first_language : Language, second_language : Language,  wordpairs : WordPair[]){
        this.id = id;
        this.name = name;
        this.first_language = first_language;
        this.second_language = second_language;
        this.wordpairs = wordpairs;
    }
}
