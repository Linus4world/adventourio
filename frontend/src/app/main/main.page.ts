import { Component } from '@angular/core';
import { Account } from '../provider/account.provider';

@Component({
  selector: 'app-main',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
})
export class MainPage {
  friends: string[] = [];

  constructor(private account: Account) { }

   ionViewWillEnter() {
     this.account.isReady.subscribe(_ => this.friends = this.account.getFriends());
  }

}
