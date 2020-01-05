import { Injectable } from '@angular/core';
import { CanLoad, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { Storage } from '@ionic/storage';
import { NavController } from '@ionic/angular';

/**
 * This service acts as a Guard for the angular router.
 * It makes sure to block the access on sites if the canLoad() function is not fulfilled.
 */
@Injectable()
export class LoadingGuard implements CanLoad {
    constructor(private storage: Storage, private navController: NavController) {}

    canLoad( _: Route): Observable<boolean> | Promise<boolean> | boolean {
        return this.storage.get('id').then(id => {
            if (!id) {
                this.navController.navigateRoot('start');
            }
            return !!id;
        });
    }
}
