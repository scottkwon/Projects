import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service'

@Component({
  selector: 'app-seattle',
  templateUrl: './seattle.component.html',
  styleUrls: ['./seattle.component.css']
})
export class SeattleComponent implements OnInit {

  constructor(private _apiService: ApiService) { }

  humidity;
  TempAvg;
  TempHigh;
  TempLow;
  Status;
  
  ngOnInit() {
    this._apiService.getWeather('Seattle')
    .then( weather => { 
      this.humidity = weather.main['humidity'];
      this.TempAvg = weather.main['temp'];
      this.TempHigh = weather.main['temp_max'];
      this.TempLow = weather.main['temp_min'];
      this.Status = weather.weather[0]['description']
     ;})
    .catch ( err => { console.log(err); })
  }

}
