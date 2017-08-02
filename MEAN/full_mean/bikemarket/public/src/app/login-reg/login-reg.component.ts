import { Component, OnInit } from '@angular/core';
import { User } from './../user';
import { UserService } from './../user.service'
import { Router } from '@angular/router'

@Component({
  selector: 'app-login-reg',
  templateUrl: './login-reg.component.html',
  styleUrls: ['./login-reg.component.css']
})
export class LoginRegComponent implements OnInit {

  regUser: User = new User();

  loginUser: User = new User();

  errors: Array<any> = [];

  constructor(private _userService: UserService, private _router: Router) { }

  ngOnInit() {
  }

  register(){
    this._userService.serviceCreateUser(this.regUser)
    .then( res => { 
      this.regUser = new User(); 
      this._router.navigate(['/bike']); 
    })
    .catch( err => {
      this.errors = JSON.parse(err._body);
    })
  }

  login(){
    this._userService.serviceLogUser(this.loginUser)
    .then( res => {
      console.log('successful log in, redirectin to bike');
      this.loginUser = new User();
      this._router.navigate(['/bike']);
    })
    .catch( err => {
      console.log("log in was DENIED!!!")
      this.errors = JSON.parse(err._body);
    })
  }
}
