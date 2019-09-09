import { Injectable } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';
import { Response } from '@angular/http';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import { catchError } from 'rxjs/operators';
import { HttpErrorHandlerService, HandleError } from '../http-error-handler.service';
import { User } from '../../model/user';
import { Language} from '../../model/language';
import { WordList} from '../../model/wordlist';
import { Subject } from 'rxjs/Subject';
import { LanguageService } from '../services/language/language.service';

@Injectable({
  providedIn: 'root'
})
export class ListService {
    private active_user : User;


    constructor(private userService : UserService, private languageService : LanguageService) { 
        userService.getActiveUser().subscribe((user) => {
            this.active_user = user;
        });
    }

    private find_language(id : number) : Language {
        return this.languageService.get_language_for_id(id)
        .then(function(language){
            return language;
        });
    }

    private json_to_wordlist(item) : WordList
        let l1 : Language = this.find_language_for_id(item.first_language);
        let l2 : Language = this.find_language_for_id(item.second_language);

        return new WordList(item.id, item.name, l1, l2, null);
    }


    public get_all_lists() : Promise<WordList[]>{
        return this.http.get<WordList>(this.wordlist_url)
        .map((response : any[]) => {
            console.log(response);
            let result : WordList[] = [];

            response.forEach(function(item){
                let l : Language = this.json_to_wordlist(item);
                result.push(l);
            });

            return result;
        }).toPromise();
    }

    /*public get_list_for_user(user_id : number) {

    }*/
}
