import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-ss',
  templateUrl: './ss.component.html',
  styleUrls: ['./ss.component.css']
})
export class SsComponent implements OnInit {

  @Input() power;

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges(){
    this.power = this.power * 90;
  }

}
