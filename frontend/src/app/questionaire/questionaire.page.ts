import { Component, ViewChild } from '@angular/core';
import { IonSlides, NavController, LoadingController } from '@ionic/angular';
import { GameProvider, Questionnaire, QuestionnaireAnswers, Session } from '../provider/game.provider';

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
  answers: QuestionnaireAnswers = {};

  constructor(private navCtrl: NavController, private game: GameProvider, private loadingController: LoadingController) {
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

  async start() {
    this.game.sendQuestionnaireAnswers(this.answers);
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

    this.game.lookingForPlayers().subscribe(
      (session: Session) => {
        console.log(session);
        this.navCtrl.navigateRoot('game');
        loading.dismiss();
      },
      error => {
        this.navCtrl.navigateRoot('main');
        loading.dismiss();
      });
  }

}
