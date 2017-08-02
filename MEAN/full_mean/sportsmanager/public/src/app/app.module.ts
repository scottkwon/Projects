import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// Remember to add modules to @NgModules.imports
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ManagerComponent } from './manager/manager.component';
import { PlayersComponent } from './manager/players/players.component';
import { ListComponent } from './manager/players/list/list.component';
import { AddComponent } from './manager/players/add/add.component';
import { StatusComponent } from './manager/status/status.component';
import { Game1Component } from './manager/status/game1/game1.component';
import { Game2Component } from './manager/status/game2/game2.component';
import { Game3Component } from './manager/status/game3/game3.component';

@NgModule({
  declarations: [
    AppComponent,
    ManagerComponent,
    PlayersComponent,
    ListComponent,
    AddComponent,
    StatusComponent,
    Game1Component,
    Game2Component,
    Game3Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
