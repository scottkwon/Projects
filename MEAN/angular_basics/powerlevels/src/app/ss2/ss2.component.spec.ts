import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Ss2Component } from './ss2.component';

describe('Ss2Component', () => {
  let component: Ss2Component;
  let fixture: ComponentFixture<Ss2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Ss2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Ss2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
