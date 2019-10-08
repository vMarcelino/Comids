import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { FoodComponent } from './food.component';

import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

describe('FoodComponent', () => {
  let component: FoodComponent;
  let fixture: ComponentFixture<FoodComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        FoodComponent,
      ],
      imports: [
        WarningMessageModule,
        HttpClientTestingModule
      ]
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FoodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
