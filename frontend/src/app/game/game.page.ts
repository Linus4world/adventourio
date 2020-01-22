import { Component, AfterViewInit, OnDestroy } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';
import { GameProvider, Quest } from '../provider/game.provider';

@Component({
  selector: 'app-game',
  templateUrl: 'game.page.html',
  styleUrls: ['game.page.scss']
})
export class GamePage implements AfterViewInit, OnDestroy {

  position: {lat: number, long: number} = {lat: 48.135124, long: 11.581981};
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
    this.geolocationProvider.trackPosition(data => this.openlayersProvider.setCenter(data.coords.latitude, data.coords.longitude));
  }

  stopTracking() {
    this.geolocationProvider.stopTracking();
  }

  receivedNewQuest(quest: Quest) {
    this.quest = quest;
    console.log('new quest:', quest);
    this.openlayersProvider.setCurrentTarget(quest.goalLocation.lat, quest.goalLocation.long);
  }

  ngAfterViewInit(): void {
    this.openlayersProvider.createMap();
    this.getPosition();
  }

  ngOnDestroy(): void {
    this.stopTracking();
  }

}
