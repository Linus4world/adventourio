import { Component, Input } from '@angular/core';
import { Challenge } from '../provider/models';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-challenge',
  templateUrl: './challenge.page.html',
  styleUrls: ['./challenge.page.scss'],
})
export class ChallengePage {
  @Input() challenge: Challenge = {
    challenge: 'Was ist ein Wolpertinger?',
    challenge_type: 1,
    answers: [
      'Ein Wolf',
      'Ein Hase',
      'Ein Vogel',
      'Ein Fabelwesen'
    ],
    right_answer: 'Ein Fabelwesen'
  };
  answer: string = undefined;

  constructor(private modalCtrl: ModalController) {
  }

  submit() {
    this.modalCtrl.dismiss(this.answer === this.challenge.right_answer);
  }

}
