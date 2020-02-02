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
    path: 'challenge', loadChildren: './modals/challenge/challenge.module#ChallengePageModule', canLoad: [LoadingGuard]
  },
  {
    path: 'story', loadChildren: './modals/story/story.module#StoryPageModule', canLoad: [LoadingGuard]
  },
  {
    path: 'feedback', loadChildren: './modals/feedback/feedback.module#FeedbackPageModule'
  },
  {
    path: '',
    redirectTo: '/main',
    pathMatch: 'full'
  },
  {
    path: 'feedback',
    loadChildren: () => import('./modals/feedback/feedback.module').then( m => m.FeedbackPageModule)
  },

];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
