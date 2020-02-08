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

  shorterStory(): string[] {
    if (this.story === undefined) {
      return undefined;
    }
    const shorterStory = [];
    for (let i = 0; i < this.story.length; i++) {
      if (i + 1 < this.story.length) {
        shorterStory.push(this.story[i] + this.story[++i]);
      } else {
        shorterStory.push(this.story[i]);
      }
    }
    return shorterStory;
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
