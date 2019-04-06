import { LanguageList } from "./languagelist";

export class Word {
    id : number;
    language_list : LanguageList;
    first_word : string;
    second_word : string;

    constructor(id : number, language_list : LanguageList, first_word : string, second_word : string){
        this.id = id;
        this.language_list = language_list;
        this.first_word = first_word;
        this.second_word = second_word;
    }
}