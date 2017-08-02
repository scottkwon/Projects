import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-quote-list',
  templateUrl: './quote-list.component.html',
  styleUrls: ['./quote-list.component.css']
})
export class QuoteListComponent implements OnInit {

  @Input() QuoteList;

  @Output() quoteDelete = new EventEmitter();

  constructor() { }

  ngOnInit() {
  }

  upvote(quote){
    quote.Rating++;
  }

  downvote(quote){
    quote.Rating--;
  }

  delete(quote){
    this.quoteDelete.emit(quote);
  }



}
