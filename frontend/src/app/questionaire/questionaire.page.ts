import { Component, OnInit, ViewChild } from '@angular/core';
import { IonSlides, NavController} from '@ionic/angular';

@Component({
  selector: 'app-questionaire-page',
  templateUrl: './questionaire.page.html',
  styleUrls: ['./questionaire.page.scss'],
})
export class QuestionairePage implements OnInit {
  @ViewChild('mySlider', {static: false}) slides: IonSlides;

  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  questions: [{id: number, question: string, options: string[]}];

  constructor(private navCtrl: NavController) {
    this.questions = [{
      id: 0,
      question: 'What genre do you like most?',
      options: [
        'Sci-fi',
        'Crime noire',
        'Super Hero'
      ]
    }];
   }

  ngOnInit() {}

  left() {
    this.slides.slidePrev();
  }

  right() {
    this.slides.slideNext();
  }

  start() {
    this.navCtrl.navigateRoot('/tab1');
  }

}
