import { Component, ViewChild } from '@angular/core';
import { IonSlides, NavController } from '@ionic/angular';
import { GameProvider, Questionnaire, QuestionnaireAnswers } from '../provider/game.provider';

@Component({
  selector: 'app-questionaire-page',
  templateUrl: './questionaire.page.html',
  styleUrls: ['./questionaire.page.scss'],
})
export class QuestionairePage {
  @ViewChild('mySlider', { static: false }) slides: IonSlides;

  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  questionnaire: Questionnaire = {questions: undefined};
  answers: QuestionnaireAnswers = {};

  constructor(private navCtrl: NavController, private game: GameProvider) {
    this.game.loadQuestionnaire().subscribe(q => {
      this.questionnaire = q;
      for (const question of this.questionnaire.questions) {
        this.answers[question.id] = question.answers[0];
      }
    });
  }

  ionViewWillEnter() {
    this.slides.slideTo(0);
  }

  left() {
    this.slides.slidePrev();
  }

  right() {
    this.slides.slideNext();
  }

  start() {
    this.game.sendQestionnaireAnswers(this.answers);
    this.navCtrl.navigateRoot('/main');
  }

}
