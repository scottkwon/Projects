import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'Mail Time!';
    
    emails = [
      {
        email: "scott@kwon.com",
        importance: true,
        subject: "Cool",
        content: "You are so cool"
      },
      {
        email: "neil@kwon.com",
        importance: false,
        subject: "Facebook",
        content: "Your campaign is doing very well!"
      },
      {
        email: "yohan@yoon.com",
        importance: false,
        subject: "Camera Inquiry",
        content: "What kind of camera are you using?"
      },
    ]
}
