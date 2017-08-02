import { Component, OnInit } from '@angular/core';
import { NoteService } from '../note.service'

@Component({
  selector: 'app-notes',
  templateUrl: './notes.component.html',
  styleUrls: ['./notes.component.css']
})
export class NotesComponent implements OnInit {

  notes: Array<any>;
  errors: Array<any>;

  constructor(private _noteService: NoteService) { }

  ngOnInit() {
    this.updateNotes()
  }
  
  updateNotes(){
    this._noteService.getNotes()
    .then( (notes) => this.notes = notes)
    .catch( err => console.log(err))
  }

  createNote(note){
    this._noteService.createNote(note)
    .then( (success)=> {
      this.updateNotes()
    })
    .catch( (err)=> {
      this.errors = err
    })
  }
}