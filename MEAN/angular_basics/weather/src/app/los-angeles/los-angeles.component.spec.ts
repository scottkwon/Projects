import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LosAngelesComponent } from './los-angeles.component';

describe('LosAngelesComponent', () => {
  let component: LosAngelesComponent;
  let fixture: ComponentFixture<LosAngelesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LosAngelesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LosAngelesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
