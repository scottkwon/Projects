import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Note } from '../../note';
import { NoteService } from '../../note.service'


@Component({
  selector: 'app-note-create',
  templateUrl: './note-create.component.html',
  styleUrls: ['./note-create.component.css']
})
export class NoteCreateComponent implements OnInit {

  newNote: Note = new Note();
  notes: Array<any> = [];
  errors: Array<any> = [];

  @Output() childEmitter = new EventEmitter();

  constructor(private _noteService: NoteService) { }

  ngOnInit() {
  }

  createNew(){
    this.childEmitter.emit(this.newNote);
    this.newNote = new Note();
  }

}
