import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Barcode Generator';

  color() {
    return '#'+(Math.random()*0xFFFFFF<<0).toString(16);
  }; 

}
