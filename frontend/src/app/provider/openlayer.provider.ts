import { Injectable } from '@angular/core';
import Map from 'ol/Map';
import View from 'ol/View';
import { fromLonLat } from 'ol/proj';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';

@Injectable()
export class OpenlayerProvider {
    /**
     * The coordinates of the point of the center of the map. The coordinates are given in EPSG:3857 format (latitude, longitude).
     * Note that the map later uses long, lat not lat, long
     */
    center: { lat: number, long: number } = { lat: 48.135124, long: 11.581981 };
    /**
     * The factor to which the map zooms. The user can later change this in the view
     */
    zoom = 13;

    map: Map;
    private view: View;

    constructor() { }

    /**
     * Creates a new Map and will link it to a div with class="map". Make sure to call this after ngAfterViewInit!
     */
    public createMap() {
        this.view = new View({
            projection: 'EPSG:3857',
            center: fromLonLat([this.center.long, this.center.lat]),
            zoom: this.zoom
        });

        this.map = new Map({
            target: 'map',
            layers: [
                new TileLayer({
                    source: new XYZ({
                        url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                    })
                })
            ],
            view: this.view
        });
    }

    /**
     * Updates the map to center the given point with the given zoom
     * @param center The coordinates of the point of the center of the map.
     * The coordinates are given in EPSG:4326 format (latitude, longitude) and will be converted to EPSG:3857.
     * Note that the map later uses long, lat not lat, long
     * @param zoom The factor to which the map zooms. The user can later change this in the view.
     */
    public setCenter(lat: number, long: number, zoom?: number) {
        this.view.setCenter(fromLonLat([long, lat]));
        if (zoom !== undefined) {
            this.view.setZoom(zoom);
        }
    }

}
