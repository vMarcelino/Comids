import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MasterDetailComponent } from './master-detail.component';
import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';
import { MasterDetailRoutingModule } from './master-detail-routing.module';

@NgModule({
  declarations: [
    MasterDetailComponent,
  ],
  imports: [
    CommonModule,
    WarningMessageModule,
    MasterDetailRoutingModule
  ]
})
export class MasterDetailModule { }
