import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ListComponent } from './list/list.component';
import { CreateComponent } from './create/create.component'
import { EditComponent } from './edit/edit.component'

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/home',
  },
  {
    path:'home',
    component: HomeComponent,
  },
  {
    path:'products',
    component: ListComponent,
  },
  {
    path:'create',
    component: CreateComponent,

  },
  {
    path:'edit/:id',
    component: EditComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
