import { Injectable } from '@angular/core';
import { CanLoad, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { Storage } from '@ionic/storage';
import { NavController } from '@ionic/angular';

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
