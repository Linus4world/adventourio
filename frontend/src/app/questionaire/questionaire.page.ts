import { Component, OnInit, ViewChild } from '@angular/core';
import { IonSlides} from '@ionic/angular';

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

  questions: {question: string, options: string[]};
  constructor() { }

  ngOnInit() {}

  left() {
    console.log('left');
    this.slides.slidePrev();
  }

  right() {
    console.log('right');
    this.slides.slideNext();
  }

}
