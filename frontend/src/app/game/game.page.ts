import { Component, AfterViewInit, NgZone } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';
import { GameProvider } from '../provider/game.provider';
import { Geoposition } from '@ionic-native/geolocation/ngx';
import { Stage } from '../provider/models';
import { Platform, ModalController, NavController } from '@ionic/angular';
import { ChallengePage } from '../challenge/challenge.page';

@Component({
  selector: 'app-game',
  templateUrl: 'game.page.html',
  styleUrls: ['game.page.scss']
})
export class GamePage implements AfterViewInit {

  stage: Stage;
  storyPointer = 0;

  constructor(
    private geolocationProvider: GeolocationProvider,
    private openlayersProvider: OpenlayerProvider,
    private gameProvider: GameProvider,
    private zone: NgZone,
    private platform: Platform,
    private navCtrl: NavController,
    public modalController: ModalController) {
    this.getNewQuest();
  }

  getPosition() {
    this.geolocationProvider.getPosition().then(pos => {
      this.openlayersProvider.setCenter(pos.coords.latitude, pos.coords.longitude, 19);
    });
  }

  startTracking() {
    this.geolocationProvider.trackPosition(data => this.positionChanged(data));
  }

  stopTracking() {
    this.geolocationProvider.stopTracking();
  }

  private positionChanged(data: Geoposition) {
    this.openlayersProvider.setPlayer(data.coords.latitude, data.coords.longitude);
    if (this.openlayersProvider.hasReachedGoal()) {
      this.gameProvider.unlockChallenge().subscribe(_ => {
        this.presentChallengePage();
      });
    }
  }

  private async getNewQuest(challengeOutcome?: boolean) {
    const coords = (await this.geolocationProvider.getPosition()).coords;
    this.gameProvider.getNextQuest(challengeOutcome, [coords.latitude, coords.longitude]).subscribe(stage => {
      console.log('new stage:', stage);
      this.zone.run(() => {
        this.stage = stage;
      });

      if (stage.challenge) {
        this.openlayersProvider.setCurrentTarget(stage.destinationCoords[0], stage.destinationCoords[1]);
      }
    });
  }

  showNextStoryPart() {
    this.storyPointer++;
    if (this.storyPointer >= this.stage.story.length && !this.stage.challenge) {
      this.navCtrl.navigateRoot('main');
    }
  }

  jumpToTarget() {
    this.gameProvider.unlockChallenge().subscribe(_ => {
      this.presentChallengePage();
    });
  }

  async presentChallengePage() {
    const modal = await this.modalController.create({
      component: ChallengePage,
      componentProps: {
        challenge: this.stage.challenge,
      }
    });
    modal.onDidDismiss().then(o => this.getNewQuest(o.data));
    return await modal.present();
  }

  ngAfterViewInit(): void {
    this.platform.ready().then(() => {
      this.openlayersProvider.createMap();
      this.getPosition();
    });
  }

  viewDidDisappear(): void {
    this.stopTracking();
  }

}
