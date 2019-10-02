import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GridComponent } from './grid.component';
import { GridRoutingModule } from './grid-routing.module';
import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

@NgModule({
  declarations: [
    GridComponent,
  ],
  imports: [
    CommonModule,
    WarningMessageModule,
    GridRoutingModule
  ]
})
export class GridModule { }
