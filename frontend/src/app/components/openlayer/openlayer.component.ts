// Solution based on https://stackoverflow.com/a/48303261

import { Component, AfterViewInit, Input } from '@angular/core';
// import { defaults as defaultControls } from 'ol/control';
// import ZoomToExtent from 'ol/control/ZoomToExtent';
import Map from 'ol/Map';
import View from 'ol/View';
import {fromLonLat} from 'ol/proj';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';


@Component({
  selector: 'openlayer',
  templateUrl: './openlayer.component.html',
  styleUrls: ['./openlayer.component.scss'],
})
export class OpenlayerComponent implements AfterViewInit {
  /**
   * The coordinates of the point of the center of the map. The coordinates are given in EPSG:3857 format (latitude, longitude).
   * Note that the map later uses long, lat not lat, long
   */
  @Input() center: {lat: number, long: number} = {lat: 48.135124, long: 11.581981};
  /**
   * The factor to which the map zooms. The user can later change this in the view
   */
  @Input() zoom = 13;

  map: Map;

  constructor() {
  }

  ngAfterViewInit() {
    this.map = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new XYZ({
            url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png'
          })
        })
      ],
      view: new View({
        projection: 'EPSG:3857',
        center: fromLonLat([this.center.long, this.center.lat]),
        zoom: this.zoom
      }),
    });
  }

}
