import { Component, ViewChild } from '@angular/core';
import { IonSlides, NavController, LoadingController } from '@ionic/angular';
import { GameProvider } from '../provider/game.provider';
import { Account } from '../provider/account.provider';
import { Questionnaire, QuestionnaireAnswers } from '../provider/models';

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

  questionnaire: Questionnaire = { questions: undefined };
  answers: QuestionnaireAnswers = {name: undefined, answers: []};

  constructor(
    private navCtrl: NavController,
    private game: GameProvider,
    private loadingController: LoadingController,
    private account: Account) {
    this.account.isReady.subscribe(() => this.answers.name = this.account.getName());

    this.game.loadQuestionnaire().subscribe(q => {
      this.questionnaire = q;
      for (let i = 0; i < this.questionnaire.questions.length; i++) {
        this.answers.answers[i] = this.questionnaire.questions[i].options[0];
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

  async start() {
    const loading = await this.loadingController.create({
      message: 'Waiting for other players...',
      spinner: 'crescent',
      backdropDismiss: true
    });
    await loading.present();

    loading.onWillDismiss().then(dismiss => {
      if (dismiss.role === 'backdrop') {
        console.warn('Exit Session!');
        this.navCtrl.navigateRoot('main');
      }
    });

    this.game.sendQuestionnaireAnswers(this.answers).subscribe(() => {
      this.navCtrl.navigateRoot('game');
      loading.dismiss();
    },
    error => {
      console.error(error);
      this.navCtrl.navigateRoot('main');
      loading.dismiss();
    });
  }

}
