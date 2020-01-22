import { Injectable } from '@angular/core';
import Map from 'ol/Map';
import View from 'ol/View';
import { fromLonLat } from 'ol/proj';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import XYZ from 'ol/source/XYZ';
import { Feature } from 'ol';
import Point from 'ol/geom/Point';
import VectorSource from 'ol/source/Vector';
import {Style, Fill, Stroke, Circle} from 'ol/style';

@Injectable()
export class OpenlayerProvider {
    /**
     * The map displayed in the html
     */
    map: Map;
    /**
     * The view of the map. Can be positioned using the setCenter() function
     */
    private view: View;
    /**
     * A marker indicating the user's current position
     */
    private marker: Feature;
    /**
     * A marker indicating the user's current target
     */
    private target: Feature;

    constructor() { }

    /**
     * Creates a new Map and will link it to a div with class="map". Make sure to call this after ngAfterViewInit!
     */
    public createMap() {
        this.marker = new Feature({
            name: 'User Position'
          });

        this.marker.setStyle(
            new Style({
                image: new Circle({
                    fill: new Fill({ color: [255, 0, 0, 1] }),
                    stroke: new Stroke({ color: [0, 0, 0, 1] }),
                    radius: 5
                })
            })
        );

        this.target = new Feature({
            name: 'Current Target'
        });

        this.target.setStyle(
            new Style({
                image: new Circle({
                    fill: new Fill({ color: [0, 0, 255, 1] }),
                    stroke: new Stroke({ color: [0, 0, 0, 1] }),
                    radius: 5
                })
            })
        );

        this.view = new View({
            projection: 'EPSG:3857',
            center: fromLonLat([11.581981, 48.135124]),
            zoom: 13
        });

        this.map = new Map({
            target: 'map',
            layers: [
                new TileLayer({
                    source: new XYZ({
                        url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                    })
                }),
                new VectorLayer({
                    source: new VectorSource({
                        features: [this.marker, this.target]
                    })
                })
            ],
            view: this.view
        });
    }

    /**
     * Updates the map to center the given point with the given zoom
     * @param lat latitude in EPSG:4326 format
     * @param long latitude in EPSG:4326 format
     * @param zoom The factor to which the map zooms. The user can later change this in the view.
     */
    public setCenter(lat: number, long: number, zoom?: number) {
        this.view.setCenter(fromLonLat([long, lat]));
        if (zoom !== undefined) {
            this.view.setZoom(zoom);
        }
        this.setMarker(lat, long);
    }

    /**
     * Sets the marker to the given position
     * @param lat latitude in EPSG:4326 format
     * @param long latitude in EPSG:4326 format
     */
    private setMarker(lat: number, long: number) {
        this.marker.setGeometry(new Point(fromLonLat([long, lat])));
    }

    /**
     * Sets the target marker to the given position.
     * @param lat latitude in EPSG:4326 format
     * @param long latitude in EPSG:4326 format
     */
    public setCurrentTarget(lat: number, long: number, unset?: boolean) {
        if (unset) {
            this.target.setGeometry(undefined);
        } else {
        this.target.setGeometry(new Point(fromLonLat([long, lat])));
        }
    }

}
