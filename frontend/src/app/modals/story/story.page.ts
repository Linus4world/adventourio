import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { IonSlides, ModalController } from '@ionic/angular';
import { GameProvider } from 'src/app/provider/game.provider';

@Component({
  selector: 'app-story',
  templateUrl: './story.page.html',
  styleUrls: ['./story.page.scss'],
})
export class StoryPage {
  @ViewChild('mySlider', { static: false }) slides: IonSlides;
  @Input() story: string[];
  storyPointer = 0;
  showSlides = false;
  character = 'Adventurer';


  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  constructor(private modalCtrl: ModalController, gameProvider: GameProvider) {
    this.character = gameProvider.getCharacter();
  }

  continue() {
    this.modalCtrl.dismiss();
  }

  ionViewWillEnter() {
    document.querySelector('app-story').classList.add(this.character);
  }

  ionViewDidEnter() {
    this.showSlides = true;
}

}
