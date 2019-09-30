import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '',   redirectTo: '/home', pathMatch: 'full' },
  {
    path: 'home',
    loadChildren: () => import('./app-shell/homePage/blank.module').then(mod => mod.BlankModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./app-shell/register/grid.module').then(mod => mod.GridModule)
  },
  {
    path: 'listPlace',
    loadChildren: () => import('./app-shell/listPlace/list.module').then(mod => mod.ListModule)
  },
  {
    path: 'listItem',
    loadChildren: () => import('./app-shell/listItem/master-detail.module').then(mod => mod.MasterDetailModule)
  },
  {
    path: 'homeIndex',
    loadChildren: () => import('./app-shell/homeIndex/home-index.module').then(mod => mod.HomeIndexModule)
  },
  {
    path: 'food',
    loadChildren: () => import('./app-shell/food/food.module').then(mod => mod.FoodModule)
  },

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule { }

