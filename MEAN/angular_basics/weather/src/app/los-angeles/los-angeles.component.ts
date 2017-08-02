import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service'

@Component({
  selector: 'app-los-angeles',
  templateUrl: './los-angeles.component.html',
  styleUrls: ['./los-angeles.component.css']
})
export class LosAngelesComponent implements OnInit {

  humidity;
  TempAvg;
  TempHigh;
  TempLow;
  Status;
  setPosition;


  constructor(private _apiService: ApiService) { }

  ngOnInit() {
    this._apiService.getWeather('LosAngeles')
    .then( weather => { 
      this.humidity = weather.main['humidity'];
      this.TempAvg = weather.main['temp'];
      this.TempHigh = weather.main['temp_max'];
      this.TempLow = weather.main['temp_min'];
      this.Status = weather.weather[0]['description'];
    })
    .catch ( err => { console.log(err); })

  }


}
