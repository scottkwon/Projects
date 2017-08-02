import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LosAngelesComponent } from './los-angeles/los-angeles.component';
// Remember to add modules to @NgModules.imports
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ApiService } from './api.service';
import { SanJoseComponent } from './san-jose/san-jose.component';
import { SeattleComponent } from './seattle/seattle.component';
import { DallasComponent } from './dallas/dallas.component';
import { ChicagoComponent } from './chicago/chicago.component';
import { WashingtonDCComponent } from './washington-dc/washington-dc.component'

@NgModule({
  declarations: [
    AppComponent,
    LosAngelesComponent,
    SanJoseComponent,
    SeattleComponent,
    DallasComponent,
    ChicagoComponent,
    WashingtonDCComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
