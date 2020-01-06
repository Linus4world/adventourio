import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';
import { Account } from './provider/account.provider';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {

  hideTabBarPages = [
    'start',
  ];
  hideTabBar = false;

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private router: Router,
    // tslint:disable-next-line:variable-name
    _account: Account // To ensure loading on start
  ) {
    this.initializeApp();
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      this.navEvents();
    });
  }

  // A simple subscription that tells us what page we're currently navigating to.
  private navEvents() {
    this.router.events.pipe(filter(e => e instanceof NavigationEnd)).subscribe((e: any) => {
      this.showHideTabs(e);
    });
  }

  private showHideTabs(e: any) {
    const urlArray = e.url.split('/');
    const pageUrl = urlArray[urlArray.length - 1];
    this.hideTabBar = this.hideTabBarPages.indexOf(pageUrl) > -1;
  }
}
