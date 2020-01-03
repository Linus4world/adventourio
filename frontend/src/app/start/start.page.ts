import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage';
import { NavController } from '@ionic/angular';
const uuidv1 = require('uuid/v1');

/**
 * Start page that will only be shown when the user logs in for the first time
 */
@Component({
  selector: 'app-start-page',
  templateUrl: './start.page.html',
  styleUrls: ['./start.page.scss'],
})
export class StartPage implements OnInit {
  name = 'Mr. NoName';
  id: string;

  constructor(private storage: Storage, private navCtrl: NavController) { }

  ngOnInit() {}

  submit() {
    this.storage.set('name', this.name);
    this.id = uuidv1();
    this.storage.set('id', this.id);
    console.log(this.name);
    console.log(this.id);
    this.navCtrl.navigateForward('/tab1');
  }

}
