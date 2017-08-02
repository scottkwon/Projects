import { Injectable } from '@angular/core';
import 'rxjs'
import { Http } from '@angular/http'

@Injectable()
export class UserService {

  constructor(private _http: Http) { }

  serviceCreateUser(user){
    return this._http.post('/api/users/register', user)
    .map( response => response.json() )
    .toPromise()
  };

  serviceLogUser(user){
    return this._http.post('/api/users/login', user)
    .map( response => response.json() )
    .toPromise()
  };

}
