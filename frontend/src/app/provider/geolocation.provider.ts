import { Geolocation, Geoposition } from '@ionic-native/geolocation/ngx';
import { Injectable } from '@angular/core';
import { Subscription } from 'rxjs';
import { filter } from 'rxjs/operators';

/**
 * This service handles user postion tracking.
 */
@Injectable()
export class GeolocationProvider {
    private watch: Subscription;

    constructor(private geolocation: Geolocation) { }

    /**
     * Returns a Promise with the current position of the user
     */
    public getPosition(): Promise<Geoposition> {
        return this.geolocation.getCurrentPosition().then((resp) => {
            console.log('[Geolocation Position]:', resp);
            return resp;
        });
    }

    /**
     * Tracks the users movement. The given callback function is executed whenever the position changes.
     * Make sure to call the stopTracking() function when you are finished to track the user.
     */
    public trackPosition(callback: (data: Geoposition) => any) {
        console.log('Start Tracking!');
        this.watch = this.geolocation.watchPosition().pipe(filter((p) => p.coords !== undefined)).subscribe((data) => {
            console.log('[Geolocation Tracking]:', data);
            callback(data);
        });
    }

    /**
     * Stops the user location tracking by unsubscribing from the Observable.
     */
    public stopTracking() {
        this.watch.unsubscribe();
        console.log('Tracking was stopped!');
    }
}
