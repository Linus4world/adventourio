import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Platform } from '@ionic/angular';
import { ReplaySubject } from 'rxjs';

export enum AccountValue {
    id = 'id',
    name = 'name',
    friends = 'friends',
    country = 'country'
}

/**
 * Stores all user information
 */
@Injectable()
export class Account {
    private values: {[key: string]: any} = {};
    public isReady = new ReplaySubject();

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
        this.isReady.next(true);
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
     * Returns the country of the user
     */
    public getCountry(): string {
        return this.values[AccountValue.country];
    }

    /**
     * Returns the friend list of the user
     */
    public getFriends(): string[] {
        const friends = this.values[AccountValue.friends];
        return friends ? friends : [];
    }

    public get(key: string): any {
        return this.values[key];
    }

    public async store(key: AccountValue, value: any): Promise<void> {
        await this.storage.set(key, value);
        this.values[key] = value;
    }
}
