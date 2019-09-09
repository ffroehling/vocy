import {Language} from './language';
import {WordList} from './wordlist';

export class WordPair {
    id : number;
    wordlist : WordList;
    first_word : string;
    second_word : string;

    constructor(id : number, wordlist : WordList, first_word : string, second_word : string){
        this.id = id;
        this.wordlist = wordlist;
        this.first_word = first_word;
        this.second_word = second_word;
    }
}
