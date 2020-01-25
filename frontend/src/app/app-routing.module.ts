import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { LoadingGuard } from './provider/loading-guard.provider';

const routes: Routes = [
  {
    path: 'start', loadChildren: './start/start.module#StartPageModule'
  },
  {
    path: 'q', loadChildren: './questionaire/questionaire.module#QuestionairePageModule'
  },
  {
    path: 'main', loadChildren: './main/main.module#MainPageModule', canLoad: [LoadingGuard]
  },
  {
    path: 'game', loadChildren: './game/game.module#GamePageModule', canLoad: [LoadingGuard]
  },
  {
    path: 'challenge', loadChildren: './challenge/challenge.module#ChallengePageModule', canLoad: [LoadingGuard]
  },
  {
    path: '',
    redirectTo: '/main',
    pathMatch: 'full'
  }
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
