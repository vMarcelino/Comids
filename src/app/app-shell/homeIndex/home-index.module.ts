import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeIndexComponent } from './home-index.component';
import { HomeIndexRoutingModule } from './home-index-routing.module';

@NgModule({
  imports: [
    CommonModule,
    HomeIndexRoutingModule,
  ],
  declarations: [
    HomeIndexComponent
  ]
})
export class HomeIndexModule { }