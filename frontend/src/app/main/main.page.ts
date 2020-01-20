import { Component } from '@angular/core';
import { Account, Friend } from '../provider/account.provider';

@Component({
  selector: 'app-main',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
})
export class MainPage {
  friends: Friend[] = [];

  constructor(account: Account) {
    // account.store(AccountValue.friends, [{id: '1', name: 'Daniela'}, {id: '2', name: 'Kim'}, {id: '3', name: 'Rudolf'}]);
    account.isReady.subscribe(_ => this.friends = account.getFriends());
   }

}
