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
import { Subject } from 'rxjs/Subject';

@Injectable({
  providedIn: 'root'
})
export class UserService {

    private user_url = "/api/user";
    private active : Subject<User> = new Subject<User>();

    //handlers
    private handleError: HandleError;

    constructor(private http: HttpClient, httpErrorHandler: HttpErrorHandlerService) {
        this.handleError = httpErrorHandler.createHandleError('PersonenService');
        //var that = this;
    }


    public loadUser() : Promise<User[]> {
        return this.http.get<User[]>(this.user_url)
        .map((response : any[]) => {
            console.log(response);
            let result : User[] = [];

            response.forEach(function(item){
                let u : User = new User(item.id, item.name);
                result.push(u);
            });

            return result;
        }).toPromise();
    }

    public setActiveUser(user) {
        this.active.next(user);
        console.log("setted");
    }

    public getActiveUser(){
        return this.active;
    }


}
