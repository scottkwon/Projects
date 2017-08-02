import { Component } from '@angular/core';
import { HttpService } from './http.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  username: string = "";
  score: number;
  err: boolean = false;

  constructor(private _httpService:HttpService){};

  findUser(){
    this._httpService.getUser(this.username)
    .then( user => (this.score = ( user.public_repos+user.followers )))
    .catch( error => (this.err=true) )
  }

}
