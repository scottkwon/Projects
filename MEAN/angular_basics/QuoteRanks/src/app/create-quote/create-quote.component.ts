import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-create-quote',
  templateUrl: './create-quote.component.html',
  styleUrls: ['./create-quote.component.css']
})
export class CreateQuoteComponent implements OnInit {

  @Input() QuoteList;

  newQuote = {Author: "", Body: "", Rating:0}

  @Output() pushQuote = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  add(formData){
    console.log("emitting***********");
    this.pushQuote.emit(this.newQuote);
    this.newQuote = {Author: "", Body: "", Rating:0}
  }

}
