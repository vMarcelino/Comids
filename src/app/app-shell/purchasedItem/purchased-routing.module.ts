import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { PurchasedComponent } from './purchased.component'

const routes: Routes = [
  {
    path: '',
    component: PurchasedComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PurchasedRoutingModule { }