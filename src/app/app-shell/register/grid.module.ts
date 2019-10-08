import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GridComponent } from './grid.component';
import { GridRoutingModule } from './grid-routing.module';

@NgModule({
  declarations: [
    GridComponent,
  ],
  imports: [
    CommonModule,
    GridRoutingModule
  ]
})
export class GridModule { }
