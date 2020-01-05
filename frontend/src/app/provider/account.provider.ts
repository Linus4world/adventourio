import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Platform } from '@ionic/angular';

/**
 * Stores all user information
 */
@Injectable()
export class Account {

    private id: string;
    private name: string;


    constructor(private storage: Storage, platform: Platform) {
        platform.ready().then(() => {
            this.update();
        });
    }

    /**
     * Loads all account informations from the local storage and assigns them to the local variables.
     */
    public update(): Promise<void> {
        console.log('Loading account information...');
        return Promise.all([
            this.storage.get('id').then(v => this.id = v),
            this.storage.get('name').then(v => this.name = v),
        ]).then(() => console.log('Loading complete!'));
    }

    /**
     * Returns the name of the user
     */
    public getName(): string {
        return '' + this.name;
    }

    /**
     * Returns the UUID of the user
     */
    public getID(): string {
        return '' + this.id;
    }
}
