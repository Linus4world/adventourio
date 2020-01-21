import { Component, OnInit, ViewChild } from '@angular/core';
import { IonSlides, NavController } from '@ionic/angular';
import { GameProvider } from '../provider/game.provider';

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

  questions: [{ id: number, question: string, answers: string[] }];
  answers = {};

  constructor(private navCtrl: NavController, private game: GameProvider) {
    this.game.loadQuestionnaire().subscribe(q => {
      this.questions = q.questions;
      for (const question of this.questions) {
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
    console.warn(this.answers);
    this.navCtrl.navigateRoot('/main');
  }

}
