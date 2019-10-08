import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { HomeIndexComponent } from './home-index.component';

import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

describe('HomeIndexComponent', () => {
  let component: HomeIndexComponent;
  let fixture: ComponentFixture<HomeIndexComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        HomeIndexComponent,
      ],
      imports: [
        WarningMessageModule,
        HttpClientTestingModule
      ]
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomeIndexComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
