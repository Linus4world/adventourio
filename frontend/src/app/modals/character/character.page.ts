import { Component, Input } from '@angular/core';
import { ModalController } from '@ionic/angular';

@Component({
  selector: 'app-character',
  templateUrl: './character.page.html',
  styleUrls: ['./character.page.scss'],
})
export class CharacterPage {
  @Input() character = 'Detective';

  constructor(private modalController: ModalController) {
  }

  continue() {
    this.modalController.dismiss();
  }

  ionViewWillEnter() {
    document.querySelector('app-character').classList.add(this.character);
  }

}
