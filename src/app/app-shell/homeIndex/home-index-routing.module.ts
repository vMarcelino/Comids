import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { HomeIndexComponent } from './home-index.component'

const routes: Routes = [
  {
    path: '',
    component: HomeIndexComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeIndexRoutingModule { }