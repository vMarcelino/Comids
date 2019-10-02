import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './footer.component';
import { FooterRoutingModule } from './footer-routing.module';
@NgModule({
  imports: [
    CommonModule,
    FooterRoutingModule
  ],
  declarations: [FooterComponent]
})
export class FooterModule { }