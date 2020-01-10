import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Platform } from '@ionic/angular';

export enum AccountValue {
    id = 'id',
    name = 'name',
    friends = 'friends'
}

/**
 * Stores all user information
 */
@Injectable()
export class Account {
    private values: {[key: string]: any} = {};

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
    public getFriends(): string[] {
        return this.values[AccountValue.friends];
    }

    public async store(key: AccountValue, value: any): Promise<void> {
        await this.storage.set(key, value);
        this.values[key] = value;
    }
}
