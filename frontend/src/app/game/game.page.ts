import { Component, AfterViewInit, NgZone } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';
import { GameProvider } from '../provider/game.provider';
import { Geoposition } from '@ionic-native/geolocation/ngx';
import { Stage } from '../provider/models';
import { Platform, ModalController, NavController, LoadingController } from '@ionic/angular';
import { ChallengePage } from '../modals/challenge/challenge.page';
import { StoryPage } from '../modals/story/story.page';
import { FeedbackPage } from '../modals/feedback/feedback.page';
import { CharacterPage } from '../modals/character/character.page';

@Component({
  selector: 'app-game',
  templateUrl: 'game.page.html',
  styleUrls: ['game.page.scss']
})
export class GamePage implements AfterViewInit {

  stage: Stage;
  character: string;

  constructor(
    private geolocationProvider: GeolocationProvider,
    private openlayersProvider: OpenlayerProvider,
    private gameProvider: GameProvider,
    private zone: NgZone,
    private platform: Platform,
    private navCtrl: NavController,
    public modalController: ModalController,
    private loadingController: LoadingController) {
    this.character = gameProvider.getCharacter();
    this.presentCharacterPage();
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
      this.presentChallengePage();
    }
  }

  private async getNewQuest(challengeOutcome?: boolean) {
    const coords = (await this.geolocationProvider.getPosition()).coords;

    const loading = await this.loadingController.create({
      message: 'Waiting for other players...',
      spinner: 'crescent',
      backdropDismiss: true
    });

    await loading.present();

    this.gameProvider.getNextQuest(challengeOutcome, [coords.latitude, coords.longitude]).subscribe(stage => {
      loading.dismiss();
      console.log('new stage:', stage);
      this.zone.run(() => {
        this.stage = stage;
        this.presentStoryPage();
      });

      if (stage.challenge) {
        this.openlayersProvider.setCurrentTarget(stage.destinationCoords[0], stage.destinationCoords[1]);
      }
    });
  }

  jumpToTarget() {
    this.presentChallengePage();
  }

  private async presentCharacterPage() {
    const modal = await this.modalController.create({
      component: CharacterPage,
      componentProps: {
        character: this.character,
      }
    });
    modal.onDidDismiss().then(() => this.getNewQuest());
    return await modal.present();
  }

  private async presentChallengePage() {
    const modal = await this.modalController.create({
      component: ChallengePage,
      componentProps: {
        challenge: this.stage.challenge,
      }
    });
    modal.onDidDismiss().then(o => this.getNewQuest(o.data));
    return await modal.present();
  }

  private async presentStoryPage() {
    console.warn(this.stage.story)
    const modal = await this.modalController.create({
      component: StoryPage,
      componentProps: {
        story: this.stage.story,
      }
    });
    modal.onDidDismiss().then(() => {
      if (this.stage.game_finished === true || !this.stage.challenge) {
        this.presentFeedbackPage();
      }
    });
    return await modal.present();
  }

  private async presentFeedbackPage() {
    const modal = await this.modalController.create({
      component: FeedbackPage
    });
    modal.onDidDismiss().then(() => {
      this.navCtrl.navigateRoot('main');
    });
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
