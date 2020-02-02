import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { Geolocation } from '@ionic-native/geolocation/ngx';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IonicStorageModule } from '@ionic/storage';
import { LoadingGuard } from './provider/loading-guard.provider';
import { HTTP } from './provider/http.provider';
import { Account } from './provider/account.provider';
import { HttpClientModule } from '@angular/common/http';
import { GeolocationProvider } from './provider/geolocation.provider';
import { OpenlayerProvider } from './provider/openlayer.provider';
import { GameProvider } from './provider/game.provider';
import { ChallengePageModule } from './modals/challenge/challenge.module';
import { StoryPageModule } from './modals/story/story.module';
import { FeedbackPageModule } from './modals/feedback/feedback.module';

@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    HttpClientModule,
    IonicModule.forRoot(),
    IonicStorageModule.forRoot(),
    AppRoutingModule,
    ChallengePageModule,
    StoryPageModule,
    FeedbackPageModule
  ],
  providers: [
    StatusBar,
    SplashScreen,
    LoadingGuard,
    HTTP,
    Account,
    Geolocation,
    GeolocationProvider,
    OpenlayerProvider,
    GameProvider,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
