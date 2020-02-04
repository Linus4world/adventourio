import { Component, Input } from '@angular/core';
import { Challenge } from '../../provider/models';
import { ModalController } from '@ionic/angular';
import { GameProvider } from 'src/app/provider/game.provider';
import { GeolocationProvider } from 'src/app/provider/geolocation.provider';
import { OpenlayerProvider } from 'src/app/provider/openlayer.provider';

@Component({
  selector: 'app-challenge',
  templateUrl: './challenge.page.html',
  styleUrls: ['./challenge.page.scss'],
})
export class ChallengePage {
  @Input() challenge: Challenge = {
    // tslint:disable-next-line:max-line-length
    challenge: 'Hans is a very old, common German name. Can you name the most common German surname?',
    challenge_type: 2,
    right_answer: [
      'Mueller',
      'Müller',
      'Muller'
    ]
  };
  answer: string = undefined;
  character: string;
  characterText = 'All right, let\'s find this place! It has to be somewhere close...';
  submitted = false;

  constructor(
    private modalCtrl: ModalController,
    gameProvider: GameProvider,
    geolocationProvider: GeolocationProvider,
    openlayerProvider: OpenlayerProvider) {
    this.character = gameProvider.getCharacter();
    if (this.challenge.challenge_type === 3) {
      geolocationProvider.trackPosition(() => {
        switch (openlayerProvider.getDistance()) {
          case 0:
            this.submit();
            break;
          case 1:
            this.characterText = 'We are very close now, I can feel it!';
            break;
          case 2:
            this.characterText = 'It is not far!';
            break;
          case 3:
            this.characterText = 'Hmm I don\'t think that is the right direction...';
            break;
          case 4:
            // this.modalCtrl.dismiss(false);
            break;
        }
      });
    }
  }

  submit() {
    this.submitted = true;
  }

  continue() {
    switch (this.challenge.challenge_type) {
      case 1:
        this.modalCtrl.dismiss(this.answer === this.challenge.right_answer);
        break;
      case 2:
        this.modalCtrl.dismiss((this.challenge.right_answer as string[]).indexOf(this.answer) >= 0);
        break;
      default:
        this.modalCtrl.dismiss(true);
    }
  }

  handleUserAnswer(value: string) {
    this.answer = value;
  }

}
