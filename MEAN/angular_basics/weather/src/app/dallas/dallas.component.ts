import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service'


@Component({
  selector: 'app-dallas',
  templateUrl: './dallas.component.html',
  styleUrls: ['./dallas.component.css']
})
export class DallasComponent implements OnInit {

  constructor(private _apiService: ApiService) { }

  humidity;
  TempAvg;
  TempHigh;
  TempLow;
  Status;

  ngOnInit() {
    this._apiService.getWeather('Dallas')
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
