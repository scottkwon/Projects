import { Injectable } from '@angular/core';
import { Http } from '@angular/http'
import "rxjs"

@Injectable()
export class HttpService {

  constructor(private _http: Http) {}

  getUser(username){
    return this._http.get('http://api.github.com/users/'+ username).map( user => user.json()).toPromise()
  }

  

}
