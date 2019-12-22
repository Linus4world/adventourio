import { Component, OnInit } from '@angular/core';
import { Storage } from '@ionic/storage';
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

  constructor(private storage: Storage) { }

  ngOnInit() {}

  submit() {
    console.log(this.name);
    this.storage.set('name', this.name);
    this.id = uuidv1();
    console.log(this.id);
    this.storage.set('id', this.id);
  }

}
