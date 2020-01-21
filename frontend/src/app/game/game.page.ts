import { Component, AfterViewInit, OnDestroy } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';

@Component({
  selector: 'app-game',
  templateUrl: 'game.page.html',
  styleUrls: ['game.page.scss']
})
export class GamePage implements AfterViewInit, OnDestroy {

  position: {lat: number, long: number} = {lat: 48.135124, long: 11.581981};

  constructor(private geolocationProvider: GeolocationProvider, private openlayersProvider: OpenlayerProvider) {}

  getPosition() {
    this.geolocationProvider.getPosition().then(pos => {
      this.openlayersProvider.setCenter(pos.coords.latitude, pos.coords.longitude, 19);
    });
  }

  startTracking() {
    this.geolocationProvider.trackPosition((data) => this.openlayersProvider.setCenter(data.coords.latitude, data.coords.longitude));
  }

  stopTracking() {
    this.geolocationProvider.stopTracking();
  }

  ngAfterViewInit(): void {
    this.openlayersProvider.createMap();
    this.getPosition();
  }

  ngOnDestroy(): void {
    this.stopTracking();
  }

}
