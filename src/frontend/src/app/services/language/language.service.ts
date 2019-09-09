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
import {Language} from '../../model/language';
import { Subject } from 'rxjs/Subject';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {
    private language_url : string = "/api/language";
    private all_languages : Language[];
    
    constructor(private http : HttpClient) { }

    private item_to_language(item) : Language {
        let l : Language = new Language(item.id, item.name);
        return l;
    }

    public get_all_languages() : Promise<Language[]>{
        return this.http.get<Language[]>(this.language_url)
        .map((response : any[]) => {
            console.log(response);
            let result : Language[] = [];

            response.forEach(function(item){
                let l : Language = this.item_to_language(item);
                result.push(l);
            });

            //store in service
            this.all_languages = result;

            return result;
        }).toPromise();
    }

    private find_language_for_id(id : number) : Language{
        if(!this.all_languages){
            return null;
        }

        for(var i = 0; i < this.all_languages.length; i++){
            if(this.all_languages[i].id == id){
                return this.all_languages[i];
            }
        }

        return null;
    }

    private load_language_for_id(id : number) : Promise<Language> {
        return this.http.get<Language>(this.language_url + '/' + id)
        .map((response : any) => {
            return this.item_to_language(response);
        }).toPromise();
    }

    public get_language_for_id(id : number) : Promise<Language> {
        let result : Language = this.find_language_for_id(id);

        if(!result){
            return this.load_language_for_id(id);
        }

        return new Promise<Language>(function(resolve, reject){
            resolve(result);
        });
    }
}
