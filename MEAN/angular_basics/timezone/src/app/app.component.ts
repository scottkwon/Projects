import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'US Time Zone Display';

  currentTime = new Date().toLocaleString('en-US');

  color = ['white', 'white', 'white', 'white'];

  changeTZ(tz, index){
    if (tz==undefined && index==undefined){
        this.currentTime = new Date().toLocaleString('en-US');
    }

    var newTime = new Date().toLocaleString('en-US', {timeZone: tz})

    this.currentTime = newTime;

    for (var i=0; i<this.color.length; i++){
        if(i == index){
            this.color[i] = 'yellow';
        } else {
            this.color[i] = 'gray';
        }
    }
  }
}
