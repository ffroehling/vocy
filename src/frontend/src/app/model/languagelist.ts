import { Languagepair } from "./languagepair";

export class LanguageList {
    id : number;
    language_pair : Languagepair;
    name : string;

    constructor(id : number, language_pair : Languagepair, name : string){
        this.id = id;
        this.language_pair = language_pair;
        this.name = name;
    }
}