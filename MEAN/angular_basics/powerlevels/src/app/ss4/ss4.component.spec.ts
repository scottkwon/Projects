import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Ss4Component } from './ss4.component';

describe('Ss4Component', () => {
  let component: Ss4Component;
  let fixture: ComponentFixture<Ss4Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Ss4Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Ss4Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
