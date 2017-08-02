import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NotesComponent } from './notes/notes.component';
import { NoteCreateComponent } from './notes/note-create/note-create.component';
import { NoteListComponent } from './notes/note-list/note-list.component';
// Remember to add modules to @NgModules.imports
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NoteService } from './note.service'


@NgModule({
  declarations: [
    AppComponent,
    NotesComponent,
    NoteCreateComponent,
    NoteListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [NoteService],
  bootstrap: [AppComponent]
})
export class AppModule { }
