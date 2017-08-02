import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: string = 'Switchboard';

  board: string[] = [ "off","off","off","off","off","off","off","off","off","off" ];

  changeColor(idx){
    if(this.board[idx] == "off"){
      this.board[idx] = "on";
    } else {
      this.board[idx] = "off";
    };
  };
}
