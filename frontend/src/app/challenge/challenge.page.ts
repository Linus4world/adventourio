import { Component, OnInit } from '@angular/core';
import { NavParams } from '@ionic/angular';
import { Quest, Challenge } from '../provider/game.provider';

@Component({
  selector: 'app-challenge',
  templateUrl: './challenge.page.html',
  styleUrls: ['./challenge.page.scss'],
})
export class ChallengePage {
  challenge: Challenge = {
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

  constructor() {
    // if (navParams.data) {
    //   this.challenge = this.navParams.data.challenge;
    // }
  }

  submit() {
    console.log(this.answer, this.answer === this.challenge.right_answer);
  }

}
