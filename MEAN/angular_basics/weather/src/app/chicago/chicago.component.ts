import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service'

@Component({
  selector: 'app-chicago',
  templateUrl: './chicago.component.html',
  styleUrls: ['./chicago.component.css']
})
export class ChicagoComponent implements OnInit {

  constructor(private _apiService: ApiService) { }

    humidity;
    TempAvg;
    TempHigh;
    TempLow;
    Status;

    ngOnInit() {
      this._apiService.getWeather('Chicago')
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
