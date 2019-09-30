import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FoodComponent } from './food.component';
import { FoodRoutingModule } from './food-routing.module';


@NgModule({
  imports: [
    CommonModule,
    FoodRoutingModule
  ],
  declarations: [FoodComponent]
})
export class FoodModule { }