import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { PowerComponent } from './power/power.component';
// Remember to add modules to @NgModules.imports
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HumanComponent } from './human/human.component';
import { SaiyanComponent } from './saiyan/saiyan.component';
import { Ss2Component } from './ss2/ss2.component';
import { SsComponent } from './ss/ss.component';
import { Ss3Component } from './ss3/ss3.component';
import { Ss4Component } from './ss4/ss4.component';

@NgModule({
  declarations: [
    AppComponent,
    PowerComponent,
    HumanComponent,
    SaiyanComponent,
    Ss2Component,
    SsComponent,
    Ss3Component,
    Ss4Component
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
