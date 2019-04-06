import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LanguagePairComponent } from './language-pair.component';

describe('LanguagePairComponent', () => {
  let component: LanguagePairComponent;
  let fixture: ComponentFixture<LanguagePairComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LanguagePairComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LanguagePairComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
