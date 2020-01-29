import { Component } from '@angular/core';
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
  name = '';
  id: string;
  country = '';
  countries = [];

  constructor(
    private navCtrl: NavController,
    private account: Account) {
      fetch('assets/data/countries.json').then(async res => res.json().then((data) => {
        for (const country of data.countries) {
          this.countries.push(country.name);
        }
      }));
    }

  handleUserNameValue(username: string) {
    this.name = username;
  }

  handleCountryValue(country: string) {
    this.country = country;
  }

  async submit() {
    this.id = uuidv1();
    await this.account.store(AccountValue.id, this.id);
    await this.account.store(AccountValue.name, this.name);
    await this.account.store(AccountValue.country, this.country);
    console.log(this.id, this.name, this.country);
    this.navCtrl.navigateForward('/main');
  }

}
