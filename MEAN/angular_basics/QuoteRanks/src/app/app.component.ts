import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  QuoteList = [
    {
      Author: "Jackie Joyner-Kersee",
      Body: "It is better to look ahead and prepare than to look back and regret.",
      Rating: 0
    },
    {
      Author: "Ralph Waldo Emerson",
      Body: "A hero is no braver than an ordinary man, but he is braver five minutes longer.",
      Rating: 0
    },
    {
      Author: "Frank Zappa",
      Body: "Everybody believes in something and everybody, by virtue of the fact that they believe in something, use that something to support their own existence.",
      Rating: 0
    }
  ];

  addQuote(newQuote){
    console.log("Parent", newQuote);
    this.QuoteList.push(newQuote);
  }

  deleteQuote(quote){
    var idx = this.QuoteList.indexOf(quote)
    this.QuoteList.splice(idx,1)
  }

}
