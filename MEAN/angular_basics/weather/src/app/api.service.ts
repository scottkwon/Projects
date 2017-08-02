import { Injectable } from '@angular/core';
import { Http } from '@angular/http'
import 'rxjs'


@Injectable()
export class ApiService {

  constructor(private _http: Http) { }

  getWeather(location){
    var unit = "&units=imperial";
    var base = "http://api.openweathermap.org/data/2.5/weather?q=";
    var key = "&&APPID=eebc7591f523e687d0bbca39baaf4cf3";
    var place = location;
    var url = base + place + key + unit;

    return this._http.get(url).map(data=>data.json()).toPromise()
  }
}
