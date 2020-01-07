import { Component, OnInit, ViewChild } from '@angular/core';
import { IonSlides, NavController} from '@ionic/angular';

@Component({
  selector: 'app-questionaire-page',
  templateUrl: './questionaire.page.html',
  styleUrls: ['./questionaire.page.scss'],
})
export class QuestionairePage {
  @ViewChild('mySlider', {static: false}) slides: IonSlides;

  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  questions: [{id: number, question: string, options: string[]}];
  answers = {};

  constructor(private navCtrl: NavController) {
    this.questions = [{
      id: 5,
      question: 'What genre do you like most?',
      options: [
        'Sci-fi',
        'Crime noire',
        'Super Hero'
      ]
    }];

    for (const question of this.questions) {
      this.answers[question.id] = question.options[0];
    }
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
    this.navCtrl.navigateRoot('/tab2');
  }

}
