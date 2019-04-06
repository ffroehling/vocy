//import { Person } from './person';
import { Injectable } from '@angular/core';
import { HttpClientModule} from '@angular/common/http';
import { Response } from '@angular/http';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import { catchError } from 'rxjs/operators';
import { HttpErrorHandlerService, HandleError } from './http-error-handler.service';
import { Language } from '../model/language';
import { Languagepair } from '../model/languagepair';
import { from } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {
    //urls
    private language_url = "/api/languages/";
    private languagepair_url = "/api/languagepair/";

    //handlers
    private handleError: HandleError;

    //data
    private languages : Language[] = [];

    constructor(private http: HttpClient, httpErrorHandler: HttpErrorHandlerService) {
        this.handleError = httpErrorHandler.createHandleError('PersonenService');
        var that = this;

       /* this.loadAllLanguages().then(function(response){
            that.languages = response;
            console.log("Promise fired")
        });*/
    }

    private loadAllLanguages() : Promise<Language[]> {
        return this.http.get<Language[]>(this.language_url)
        .map((response : any[]) => {
            let result : Language[] = [];

            response.forEach(function(item){
                let l : Language = new Language(item.id, item.name);
                result.push(l);
            });

            return result;
        }).toPromise();
    }


    public loadLanguagePairs() : Promise<Languagepair[]>{
        var that = this;

        if(this.languages.length == 0){
            return this.loadAllLanguages().then(function(response){
                that.languages = response;
                console.log("All languages loaded");
                console.log(response);
            }).then(function(){
                return that.loadLanguagePairs();
            });
        }
        else {
            return this.http.get<Languagepair[]>(this.languagepair_url)
            .map((response : any[]) => {
                console.log(response);
                let result : Languagepair[] = [];
    
                response.forEach(function(item){
                    console.log(item);
                    let l1 : Language = that.getLanguageForId(item.first);
                    let l2 : Language = that.getLanguageForId(item.second);
    
    
                    let lp : Languagepair = new Languagepair(item.id, l1, l2);
                    result.push(lp);
                });
    
                return result;
            })
            .pipe(
                catchError(this.handleError('loadLanguages', []))
            )
            .toPromise();
        }
        
    }

    private getLanguageForId(id : number){
        let result : Language = null;

        this.languages.forEach(function(language){
            console.log(language.id);
            console.log(id);
            if(language.id == id){
                result = language;
                console.log("found");
                return result;
            }
        });

        return result;
    }

    /*
    public loadPersons() : Observable<Person[]> {
        return this.http.get<Person[]>(this.url)
        .map((response : any[]) => {
            console.log(response);
            let result : Person[] = [];

            response.forEach(function(item){
                let p : Person = new Person(item.id, item.firstname, item.lastname, null, item.publickey);
                result.push(p);
            });

            return result;
        })
        .pipe(
            catchError(this.handleError('loadPersons', []))
        );

    }

    public createPerson(p : Person) : Observable<Boolean> {
            return this.http.post(this.url, JSON.stringify({
                firstname: p.firstname,
                lastname: p.lastname,
                publickey : p.publickey
            }))
            .map((response : Response) => {
                p.id = response['id'];
                return true;
            })
            .pipe(
                catchError(this.handleError('createPerson', false))
            );
    }


    public deletePerson (person : Person): Observable<Boolean> {

        return this.http.delete(this.url + person.id + '/')
        .map((response : Response) => {
            return true;
        })
        .pipe(
        catchError(this.handleError('deletePerson', false))
        );
      }

    public loadKeyInformation(id : number) : Observable<any>{
            
        return this.http.get(this.url + id + '/qrcode/')
        .map((response : any[]) => {
            return response;
        })
        .pipe(
            catchError(this.handleError('loadKey', {}))
        );
    } */
}
