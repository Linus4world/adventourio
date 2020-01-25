import { Component, AfterViewInit, OnDestroy } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';
import { GameProvider, Quest } from '../provider/game.provider';
import { Geoposition } from '@ionic-native/geolocation/ngx';

@Component({
  selector: 'app-game',
  templateUrl: 'game.page.html',
  styleUrls: ['game.page.scss']
})
export class GamePage implements AfterViewInit {

  quest: Quest;

  constructor(
    private geolocationProvider: GeolocationProvider,
    private openlayersProvider: OpenlayerProvider,
    private gameProvider: GameProvider) {
    this.gameProvider.getNextQuest().subscribe((quest: Quest) => this.receivedNewQuest(quest));
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
    this.openlayersProvider.setCenter(data.coords.latitude, data.coords.longitude);
    if (this.openlayersProvider.hasReachedGoal()) {
      // TODO
    }
  }

  receivedNewQuest(quest: Quest) {
    this.quest = quest;
    console.log('new quest:', quest);
    this.openlayersProvider.setCurrentTarget(quest.goalLocation[0], quest.goalLocation[1]);
  }

  ngAfterViewInit(): void {
    this.openlayersProvider.createMap();
    this.getPosition();
  }

  viewDidDisappear(): void {
    this.stopTracking();
  }

}
