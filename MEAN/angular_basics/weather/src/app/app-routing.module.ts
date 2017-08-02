import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LosAngelesComponent } from './los-angeles/los-angeles.component'
import { SanJoseComponent } from './san-jose/san-jose.component'
import { SeattleComponent } from './seattle/seattle.component'
import { DallasComponent } from './dallas/dallas.component'
import { ChicagoComponent } from './chicago/chicago.component'
import { WashingtonDCComponent } from './washington-dc/washington-dc.component'


const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/LosAngeles',
  },
  {
    path: 'LosAngeles',
    component: LosAngelesComponent,
  },
  {
    path: 'SanJose',
    component: SanJoseComponent,
  },
  {
    path: 'Seattle',
    component: SeattleComponent,
  },
  {
    path: 'Dallas',
    component: DallasComponent,
  },
  {
    path: 'Chicago',
    component: ChicagoComponent,
  },
  {
    path: 'WashingtonDC',
    component: WashingtonDCComponent,
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
