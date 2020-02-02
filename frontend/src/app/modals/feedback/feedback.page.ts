import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-feedback',
  templateUrl: './feedback.page.html',
  styleUrls: ['./feedback.page.scss'],
})
export class FeedbackPage implements OnInit {
  feedbacks = [
    'Story',
    'Sights',
    'Challenges'
  ];

  rating = [0, 0, 0];

  constructor(private modalCtrl: ModalController) { }

  ngOnInit() {
  }

  getArray(length: number) {
    return Array(length);
  }

  rate(ratingIndex: number, rate: number) {
    this.rating[ratingIndex] = rate;
  }

  submit() {
    this.modalCtrl.dismiss();
  }

}
