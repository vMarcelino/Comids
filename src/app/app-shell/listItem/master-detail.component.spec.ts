import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { MasterDetailComponent } from './master-detail.component';

import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';

describe('MasterDetailComponent', () => {
  let component: MasterDetailComponent;
  let fixture: ComponentFixture<MasterDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        MasterDetailComponent,
      ],
      imports: [
        WarningMessageModule,
        HttpClientTestingModule
      ]
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MasterDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
