import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { QuestionairePage } from './questionaire.page';

describe('QuestionairePageComponent', () => {
  let component: QuestionairePage;
  let fixture: ComponentFixture<QuestionairePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuestionairePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(QuestionairePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
