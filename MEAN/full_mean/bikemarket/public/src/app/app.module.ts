import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginRegComponent } from './login-reg/login-reg.component';
import { BikeComponent } from './bike/bike.component';
import { BrowseComponent } from './bike/browse/browse.component';
import { ListingsComponent } from './bike/listings/listings.component';
import { LandingComponent } from './landing/landing.component';
// Remember to add modules to @NgModules.imports
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { UserService } from './user.service'

@NgModule({
  declarations: [
    AppComponent,
    LoginRegComponent,
    BikeComponent,
    BrowseComponent,
    ListingsComponent,
    LandingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
