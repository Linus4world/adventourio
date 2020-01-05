import { Component, AfterViewInit } from '@angular/core';
import { GeolocationProvider } from '../provider/geolocation.provider';
import { OpenlayerProvider } from '../provider/openlayer.provider';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page implements AfterViewInit {

  position: {lat: number, long: number} = {lat: 48.135124, long: 11.581981};

  constructor(private geolocationProvider: GeolocationProvider, private openlayersProvider: OpenlayerProvider) {}

  getPosition() {
    this.geolocationProvider.getPosition().then(pos => {
      this.openlayersProvider.setCenter(pos.coords.latitude, pos.coords.longitude, 19);
    });
  }

  startTracking() {
    this.geolocationProvider.trackPosition();
  }

  stopTracking() {
    this.geolocationProvider.stopTracking();
  }

  ngAfterViewInit(): void {
    this.openlayersProvider.createMap();
  }

}
