import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Ss3Component } from './ss3.component';

describe('Ss3Component', () => {
  let component: Ss3Component;
  let fixture: ComponentFixture<Ss3Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Ss3Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Ss3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
