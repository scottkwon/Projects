import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ManagerComponent } from './manager/manager.component';
import { PlayersComponent } from './manager/players/players.component';
import { ListComponent } from './manager/players/list/list.component';
import { AddComponent } from './manager/players/add/add.component';
import { StatusComponent } from './manager/status/status.component';
import { Game1Component } from './manager/status/game1/game1.component';
import { Game2Component } from './manager/status/game2/game2.component';
import { Game3Component } from './manager/status/game3/game3.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/players/list'
  },
  {
    path: 'players',
    component: PlayersComponent,
    children:[
      {path: 'list', component: ListComponent},
      {path: 'add', component: AddComponent}
    ]
  },
  {
    path: 'status',
    component: StatusComponent,
    children:[
      {path: 'game1', component: Game1Component},
      {path: 'game2', component: Game2Component},
      {path: 'game3', component: Game3Component}
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
