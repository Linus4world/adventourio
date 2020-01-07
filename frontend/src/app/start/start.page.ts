import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage';
import { NavController } from '@ionic/angular';
import { Account, AccountValue } from '../provider/account.provider';
const uuidv1 = require('uuid/v1');

/**
 * Start page that will only be shown when the user logs in for the first time
 */
@Component({
  selector: 'app-start-page',
  templateUrl: './start.page.html',
  styleUrls: ['./start.page.scss'],
})
export class StartPage {
  name = 'Mr. NoName';
  id: string;

  constructor(
    private navCtrl: NavController,
    private account: Account) { }

  async submit() {
    await this.account.store(AccountValue.name, this.name);
    this.id = uuidv1()
    console.log(this.id);
    console.log(this.name);
    await this.account.store(AccountValue.id, this.id);
    this.navCtrl.navigateForward('/q');
  }

}
