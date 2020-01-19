import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Platform } from '@ionic/angular';
import { Subject } from 'rxjs';

export enum AccountValue {
    id = 'id',
    name = 'name',
    friends = 'friends'
}

export interface Friend {
    id: string;
    name: string;
}

/**
 * Stores all user information
 */
@Injectable()
export class Account {
    private values: {[key: string]: any} = {};
    public isReady = new Subject();

    constructor(private storage: Storage, platform: Platform) {
        platform.ready().then(() => {
            this.update();
        });
    }

    /**
     * Loads all account informations from the local storage and assigns them to the local variables.
     */
    public async update(): Promise<void> {
        console.log('Loading account information...');
        for (const key of Object.values(AccountValue)) {
            await this.storage.get(key).then(v => this.values[key] = v);
        }
        this.isReady.next(true);
        console.log('Loading complete!');
    }

    /**
     * Returns the name of the user
     */
    public getName(): string {
        return this.values[AccountValue.name];
    }

    /**
     * Returns the UUID of the user
     */
    public getID(): string {
        return this.values[AccountValue.id];
    }

    /**
     * Returns the friend list of the user
     */
    public getFriends(): Friend[] {
        return this.values[AccountValue.friends];
    }

    public async store(key: AccountValue, value: any): Promise<void> {
        await this.storage.set(key, value);
        this.values[key] = value;
    }
}
