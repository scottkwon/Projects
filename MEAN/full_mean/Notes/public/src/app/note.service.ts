import { Injectable } from '@angular/core';
import { Http } from '@angular/http'
import 'rxjs'

@Injectable()
export class NoteService {

  constructor(private _http: Http) { }

  createNote(note){
    return this._http.post('/api/notes', note)
      .map( (response) => response.json())
      .toPromise()
    
  }

  getNotes(){
    return this._http.get('/api/notes')
      .map( (response) => response.json())
      .toPromise()
  }
}
