import { Geolocation, Geoposition } from '@ionic-native/geolocation/ngx';
import { Injectable } from '@angular/core';
import { Subscription, Observable } from 'rxjs';
import { filter, tap } from 'rxjs/operators';

/**
 * This service handles user postion tracking.
 */
@Injectable()
export class GeolocationProvider {
    private watchPosition: Observable<Geoposition>;
    private subscriptions: Subscription[] = [];

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
        if ( this.watchPosition === undefined) {
            this.watchPosition = this.geolocation.watchPosition().pipe(
                filter((p) => p.coords !== undefined),
                tap((data) => console.log('[Geolocation Tracking]:', data)));
        }
        console.log('Start Tracking!');
        this.subscriptions.push(this.watchPosition.subscribe((data) => {
            callback(data);
        }));
    }

    /**
     * Stops the user location tracking by unsubscribing from the Observable.
     */
    public stopTracking() {
        for (const sub of this.subscriptions) {
            sub.unsubscribe();
        }
        this.watchPosition = undefined;
        console.log('Tracking was stopped!');
    }
}
