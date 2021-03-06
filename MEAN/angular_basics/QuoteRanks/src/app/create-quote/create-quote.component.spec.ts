import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateQuoteComponent } from './create-quote.component';

describe('CreateQuoteComponent', () => {
  let component: CreateQuoteComponent;
  let fixture: ComponentFixture<CreateQuoteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateQuoteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateQuoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
