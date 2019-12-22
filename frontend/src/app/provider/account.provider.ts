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

    public update(): Promise<void> {
        console.log('Loading account information...');
        return Promise.all([
            this.storage.get('id').then(v => this.id = v),
            this.storage.get('name').then(v => this.name = v),
        ]).then(() => console.log('Loading complete!'));
    }

    public getName(): string {
        return '' + this.name;
    }

    public getID(): string {
        return '' + this.id;
    }
}
