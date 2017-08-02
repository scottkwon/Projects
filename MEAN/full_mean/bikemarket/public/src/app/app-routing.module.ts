import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginRegComponent } from './login-reg/login-reg.component';
import { BikeComponent } from './bike/bike.component';
import { BrowseComponent } from './bike/browse/browse.component';
import { ListingsComponent } from './bike/listings/listings.component';
import { LandingComponent } from './landing/landing.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: LandingComponent
  },
  {
    path:'bike',
    component: BikeComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
