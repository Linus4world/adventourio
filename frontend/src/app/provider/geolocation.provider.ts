import { Geolocation, Geoposition } from '@ionic-native/geolocation/ngx';
import { Injectable } from '@angular/core';
import { Subscription } from 'rxjs';

@Injectable()
export class GeolocationProvider {
    private watch: Subscription;

    constructor(private geolocation: Geolocation) { }

    public getPosition(): Promise<Geoposition> {
        return this.geolocation.getCurrentPosition().then((resp) => {
            return resp;
        });
    }

    public trackPosition() {
        console.log('Start Tracking!');
        this.watch = this.geolocation.watchPosition().subscribe((data) => {
            // data can be a set of coordinates, or an error (if an error occurred).
            // data.coords.latitude
            // data.coords.longitude
            console.log('Geoposition: ', data);
        });
    }

    public stopTracking() {
        this.watch.unsubscribe();
        console.log('Tracking was stopped!');
    }
}
