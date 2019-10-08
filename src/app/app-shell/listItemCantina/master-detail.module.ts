import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MasterDetailComponent } from './master-detail.component';
import { MasterDetailRoutingModule } from './master-detail-routing.module';

@NgModule({
  declarations: [
    MasterDetailComponent,
  ],
  imports: [
    CommonModule,
    MasterDetailRoutingModule
  ]
})
export class MasterDetailModule { }
