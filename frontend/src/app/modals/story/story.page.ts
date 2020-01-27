import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { IonSlides, ModalController } from '@ionic/angular';

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


  slideOpts = {
    initialSlide: 0,
    speed: 400
  };

  constructor(private modalCtrl: ModalController) { }

  continue() {
    this.modalCtrl.dismiss();
  }
  ionViewDidEnter() {
    this.showSlides = true;
}

}
